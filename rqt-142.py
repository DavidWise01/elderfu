#!/usr/bin/env python3
"""RQT-142: ambient cyclic H1 and exact primitive-to-ambient comparison.
Run alongside rqt-133.py and rqt-136.py with their dependencies.
"""
from pathlib import Path
from runpy import run_path
from itertools import product
import sympy as s,json
from sympy.matrices.normalforms import smith_normal_form,hermite_normal_form
from sympy.polys.domains import ZZ
p=Path(__file__).resolve().parent
X=run_path(str(p/'rqt-133.py'))['X']
Z=run_path(str(p/'rqt-136.py'))['Z']
I=s.eye(22);N=I+X+X**2+X**3
assert X**4==I and N.rank()==1 and abs(Z.det())==512
row=next(N.row(i) for i in range(22) if any(N.row(i)))
T=s.Matrix([list(row/s.igcd(*[int(x) for x in row]))]);V=I.copy()
for j in range(1,22):
 a,b=T[0,0],T[0,j]
 if b==0:continue
 u,v,g=s.gcdex(a,b)
 c,d=T[:,0],T[:,j]
 T[:,0]=u*c+v*d;T[:,j]=(-b/g)*c+(a/g)*d
 c,d=V[:,0],V[:,j]
 V[:,0]=u*c+v*d;V[:,j]=(-b/g)*c+(a/g)*d
assert abs(T[0,0])==1 and all(T[0,j]==0 for j in range(1,22))
assert abs(V.det())==1 and N*V[:,1:]==s.zeros(22,21)
M=V.inv()*(X-I)
assert M[:1,:]==s.zeros(1,22)
C=M[1:,:]
D=smith_normal_form(C,domain=ZZ)
factors=[abs(int(D[j,j])) for j in range(21)]
assert factors==[1]*15+[4]*6
F=hermite_normal_form(C);Fi=F.inv()
assert abs(F.det())==4096
res=lambda v:tuple(s.Rational(t)%1 for t in v)
six=[0,2,3,4,5,6]
survivors=[]
for j in six:
 c=Fi*(V.inv()*Z[:,j+1])[1:,:]
 assert all((2*t).is_Integer for t in c)
 assert any(not t.is_Integer for t in c)
 survivors.append(c)
classes=set()
for bits in product((0,1),repeat=6):
 c=sum((bits[j]*survivors[j] for j in range(6)),s.zeros(21,1))
 classes.add(res(c))
assert len(classes)==64
# The eight RQT-139 fixed-glue differences become ambient coboundaries.
e=s.eye(22)
glue=s.Matrix.hstack(2*e[:,0],*[e[:,j]-e[:,0] for j in (1,2,4,10,11,16)],e[:,20])
for j in range(8):
 v=Fi*(V.inv()*(X-I)*glue[:,j])[1:,:]
 assert all(t.is_Integer for t in v)
out={'RQT':142,'H1_primitive':'(Z/2)^14',
'H1_ambient':'(Z/4)^6','ambient_order':4096,
'Smith_invariants':factors,'kernel_of_map':'(Z/2)^8',
'image_of_map':'(Z/2)^6','survivors':six,
'image_classes':64,'cokernel':'(Z/2)^6',
'extension':'non-split','Hodge_conjecture':'OPEN'}
(p/'rqt-142-results.json').write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
