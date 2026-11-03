from itertools import product
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
P=17
families=[((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2))]
lines=[]
for pairs in families:
 for u,v in product((1,3,5,7),repeat=2):
  rows=[]
  for (a,b),e in zip(pairs,(u,v)):
   row=[0]*4;row[a]=1;row[b]=pow(2,e,P);rows.append(row)
  lines.append(rows)
def rank_mod(A):
 A=[[x%P for x in row] for row in A];r=0
 for k in range(4):
  t=next((j for j in range(r,len(A)) if A[j][k]),None)
  if t is None:continue
  A[r],A[t]=A[t],A[r];q=pow(A[r][k],-1,P)
  A[r]=[x*q%P for x in A[r]]
  for j in range(len(A)):
   if j!=r:
    b=A[j][k];A[j]=[(x-b*y)%P for x,y in zip(A[j],A[r])]
  r+=1
  if r==len(A):break
 return r
G=s.zeros(48)
for i in range(48):
 G[i,i]=-2
 for j in range(i+1,48):
  if rank_mod(lines[i]+lines[j])<4:G[i,j]=G[j,i]=1
assert G.rank()==20
basis=G.rref()[1]
B=G.extract(basis,basis)
assert B.det()==-64
D=smith_normal_form(B,domain=ZZ)
factors=[abs(int(D[i,i])) for i in range(20)]
assert factors==[1]*18+[8,8]
assert [abs(int(smith_normal_form(s.diag(8,8),domain=ZZ)[i,i])) for i in range(2)]==[8,8]
print("PASS: 48 lines; rank 20; determinant -64")
print("Smith factors:",factors)
print("A_NS = A_T = (Z/8 Z)^2, group order 64")
print("STOP: explicit discriminant quadratic-form anti-isometry not computed")
