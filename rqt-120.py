#!/usr/bin/env python3
"""Exact RQT-120 vertex-pairing reduction, conditional on prior geometry."""
import runpy,sympy as s,json
from pathlib import Path
p=Path(__file__).resolve().parent
r=runpy.run_path(str(p/'rqt-119.py'));g=runpy.run_path(str(p/'rqt-114.py'))
G=r['G'];piv=G.rref()[1];B=G.extract(piv,piv);Bi=B.inv()
M=G.extract(r['zero_D'],piv)*Bi
N=s.Matrix.hstack(*M.nullspace())
assert N.shape==(20,2)
a,b=s.symbols('a b',integer=True)
v=N*s.Matrix([a,b]); allv=G[:,piv]*Bi*v
P=17
def canon(rows):
 rows=[[int(x)%P for x in row] for row in rows];k=0
 for col in range(4):
  j=next((j for j in range(k,len(rows)) if rows[j][col]),None)
  if j is None:continue
  rows[k],rows[j]=rows[j],rows[k]
  inv=pow(rows[k][col],-1,P)
  rows[k]=[x*inv%P for x in rows[k]]
  for j in range(len(rows)):
   if j!=k:
    f=rows[j][col];rows[j]=[(x-f*y)%P for x,y in zip(rows[j],rows[k])]
  k+=1
 return tuple(map(tuple,rows[:k]))
lines=r['lines'];index={canon(x[-1]):i for i,x in enumerate(lines)}
perm=[]
for L in lines:
 transformed=[[row[0]*pow(4,-1,P)%P]+row[1:] for row in L[-1]]
 perm.append(index[canon(transformed)])
assert len(set(perm))==48
assert all(G[i,j]==G[perm[i],perm[j]] for i in range(48) for j in range(48))
inverse=[perm.index(i) for i in range(48)]
rotall=s.Matrix([allv[inverse[j]] for j in range(48)])
assert all(rotall[j]==0 for j in r['zero_R'])
rot=s.Matrix([rotall[j] for j in piv])
q=s.factor((v.T*Bi*v)[0])
cross=s.factor((v.T*Bi*rot)[0])
assert s.factor(cross-a*a+a*b-b*b)==0
assert s.simplify((rot.T*Bi*rot)[0]-q)==0
choices=[(x,y) for x in range(-8,9) for y in range(-8,9) if x*x-x*y+y*y==1]
assert len(choices)==6
U=g['U'];R=Bi*G.extract(piv,[perm[j] for j in piv]);J=s.Matrix([[0,-1],[1,0]])
assert R.T*B*R==B
assert all(z.is_Integer for z in R*U-U*J)
accepted=[]
for x,y in choices:
 d=N*s.Matrix([x,y]);c=Bi*d
 norm=s.factor(-2-(d.T*Bi*d)[0])
 z=int(8*norm)
 options=[(k,l) for k in range(-8,9) for l in range(-8,9) if k*k+l*l==z and all(w.is_Integer for w in c-U*s.Matrix([k,l]))]
 if options:accepted.append([x,y,str(norm),options])
assert len(accepted)==4
print(json.dumps({'NS_rank':20,'disjoint_line_constraint_rank':int(M.rank()),'free_variables':['a','b'],'algebraic_square':str(q),'cross':str(cross),'equation':'a^2-a*b+b^2=1','six_integer_solutions':choices,'four_in_chosen_abstract_gluing':accepted,'vertex_local_signs':'NOT COMPUTED','general_Hodge':'OPEN'},indent=2))
