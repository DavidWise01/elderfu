#!/usr/bin/env python3
"""RQT-144 reproducible exact four-tick cyclic-cohomology transport."""
from pathlib import Path
from runpy import run_path
from itertools import product
import sympy as s,json
from sympy.matrices.normalforms import hermite_normal_form
p=Path(__file__).resolve().parent
q=run_path(str(p/'rqt-133.py'))
r=run_path(str(p/'rqt-136.py'))
X,Z=q['X'],r['Z']
I=s.eye(22);N=I+X+X**2+X**3
row=next(N.row(i) for i in range(22) if any(N.row(i)))
row=row/s.igcd(*(int(x) for x in row))
T=s.Matrix([list(row)]);V=I.copy()
for j in range(1,22):
 a,b=T[0,0],T[0,j]
 if b==0:continue
 u,v,g=s.gcdex(a,b)
 c,d=T[:,0],T[:,j];T[:,0]=u*c+v*d;T[:,j]=(-b/g)*c+(a/g)*d
 c,d=V[:,0],V[:,j];V[:,0]=u*c+v*d;V[:,j]=(-b/g)*c+(a/g)*d
assert abs(V.det())==1 and all(T[0,j]==0 for j in range(1,22))
K=V[:,1:]
assert N*K==s.zeros(22,21)
C=(V.inv()*(X-I))[1:,:]
F=hermite_normal_form(C);Fi=F.inv()
assert abs(F.det())==4096
selected=(0,1,9,10,15,19)
Y=s.Matrix.hstack(*(s.eye(21)[:,i] for i in selected))
U=K*Y
def coords(v):
 z,par=K.gauss_jordan_solve(v)
 assert par.rows==0 and all(t.is_Integer for t in z)
 return z
def rem(v):return tuple(s.Rational(t)%1 for t in v)
states=[]
for j in range(6):
 u=U[:,j];orbit=[]
 for tick in range(5):
  state=X**tick*u
  witness=sum((X**z*u for z in range(tick)),s.zeros(22,1))
  assert state-u==(X-I)*witness
  assert rem(Fi*coords(state))==rem(Fi*Y[:,j])
  assert N*state==s.zeros(22,1)
  orbit.append([int(t) for t in state])
 assert orbit[0]==orbit[4]
 states.append(orbit)
assert X**4==I
classes=set()
for t in product(range(4),repeat=6):
 v=sum((t[j]*Fi*Y[:,j] for j in range(6)),s.zeros(21,1))
 classes.add(rem(v))
assert len(classes)==4096
survivors=[Fi*coords(Z[:,j+1]) for j in (0,2,3,4,5,6)]
changes=[]
for sv in survivors:
 matches=[mask for mask in range(64) if
  rem(sum((((mask>>j)&1)*2*Fi*Y[:,j] for j in range(6)),s.zeros(21,1)))==rem(sv)]
 assert len(matches)==1
 changes.append(matches[0])
M=s.Matrix([[int((changes[j]>>i)&1) for j in range(6)] for i in range(6)])
assert M.det()%2==1
out={'RQT':144,'six_generator_orbits':states,'return_6_of_6':True,
 'coboundary_witnesses':24,'H1_action':'identity',
 'distinct_cohomology_classes':4096,
 'double_comparison_F2':[[int(x) for x in row] for row in M.tolist()],
 'comparison_det_mod2':1,'general_Hodge':'OPEN'}
(p/'rqt-144-results.json').write_text(json.dumps(out,indent=2))
print('PASS six integer orbits, 24 coboundaries, 4096 H1 classes, doubles rank 6')
