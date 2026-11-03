#!/usr/bin/env python3
"""RQT-114: exact Fermat quartic NS--T discriminant-form gluing."""
from itertools import product
from collections import deque
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

P=17
pairs=[((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2))]
lines=[]
for matching in pairs:
 for a,b in product((1,3,5,7),repeat=2):
  rows=[]
  for (i,j),k in zip(matching,(a,b)):
   r=[0]*4;r[i]=1;r[j]=pow(2,k,P);rows.append(r)
  lines.append(rows)
def rankmod(rows):
 A=[[x%P for x in row] for row in rows];t=0
 for j in range(4):
  p=next((k for k in range(t,len(A)) if A[k][j]),None)
  if p is None:continue
  A[t],A[p]=A[p],A[t];inv=pow(A[t][j],-1,P)
  A[t]=[x*inv%P for x in A[t]]
  for k in range(len(A)):
   if k!=t:
    c=A[k][j];A[k]=[(x-c*y)%P for x,y in zip(A[k],A[t])]
  t+=1
  if t==len(A):break
 return t
G=s.zeros(48)
for i in range(48):
 G[i,i]=-2
 for j in range(i+1,48):
  if rankmod(lines[i]+lines[j])<4:G[i,j]=G[j,i]=1
piv=G.rref()[1];B=G.extract(piv,piv)
assert len(piv)==20 and B.det()==-64
D=smith_normal_form(B,domain=ZZ)
assert [abs(int(D[i,i])) for i in range(20)]==[1]*18+[8,8]
V=B.inv()
mod=lambda v:tuple(x-s.floor(x) for x in v)
zero=(s.Rational(0),)*20
cols=[mod(V[:,i]) for i in range(20)]
classes={zero};queue=deque([zero])
while queue:
 w=queue.popleft()
 for c in cols:
  z=mod([x+y for x,y in zip(w,c)])
  if z not in classes:classes.add(z);queue.append(z)
assert len(classes)==64
bil=lambda x,y:(s.Matrix(x).T*B*s.Matrix(y))[0]
good=[x for x in classes if (bil(x,x)+s.Rational(1,8))/2 in s.ZZ]
solution=None
for u in good:
 for v in good:
  if bil(u,v) not in s.ZZ:continue
  span={mod([i*x+j*y for x,y in zip(u,v)]) for i,j in product(range(8),repeat=2)}
  if len(span)==64:solution=(u,v);break
 if solution:break
assert solution
u,v=solution
U=s.Matrix.hstack(s.Matrix(u),s.Matrix(v))
C=B*U
H=B.row_join(C).col_join(C.T.row_join(U.T*B*U+s.diag(s.Rational(1,8),s.Rational(1,8))))
assert all(x in s.ZZ for x in H)
assert all(H[i,i]/2 in s.ZZ for i in range(22))
assert H.det()==-1
for a,b in product(range(8),repeat=2):
 w=mod([a*x+b*y for x,y in zip(u,v)])
 assert (bil(w,w)+s.Rational(a*a+b*b,8))/2 in s.ZZ
print({'pivot_indices':list(piv),'q_u':str(bil(u,u)),'q_v':str(bil(v,v)),
       'cross':str(bil(u,v)),'cosets':64,'det':H.det(),
       'even':True,'integral':True,
       'status':'PASS explicit 22D even unimodular gluing; NOT general Hodge proof'})
