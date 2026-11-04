#!/usr/bin/env python3
"""RQT-130: explicit non-Weyl integral isometry, in actual 20-line basis.
Run beside rqt-114.py. All assertions use exact SymPy.
"""
from itertools import product
from pathlib import Path
from runpy import run_path
import sympy as s
import json
p=Path(__file__).resolve().parent
base=run_path(str(p/'rqt-114.py'))
B,U=base['B'],base['U']
v1=s.Matrix([0,3,1,2,1,2,1,-1,-3,-2,0,2,2,0,2,2,0,0,0,0])
v2=s.Matrix([-1,-1,0,0,3,4,1,0,1,1,2,-2,0,2,2,0,0,0,0,0])
def reflection(v):
 assert (v.T*B*v)[0]==-8
 assert all(int(t)%4==0 for t in B*v)
 R=s.eye(20)+v*(v.T*B)/4
 assert all(t.is_Integer for t in R)
 assert R.T*B*R==B and R*R==s.eye(20)
 assert R.det(method='domain-ge')==-1
 return R
R1,R2=reflection(v1),reflection(v2)
W=R1*R2
assert W.T*B*W==B and W.det(method='domain-ge')==1
def finite(W):
 cols=[]
 for j in range(2):
  hit=[(a,b) for a,b in product(range(8),repeat=2)
       if all(x.is_Integer for x in W*U[:,j]-U*s.Matrix([a,b]))]
  assert len(hit)==1
  cols.append(hit[0])
 return s.Matrix([[cols[0][0],cols[1][0]],[cols[0][1],cols[1][1]]])
assert finite(R1)==s.Matrix([[7,4],[4,1]])
assert finite(R2)==s.Matrix([[1,0],[0,7]])
Q=s.Matrix([[7,4],[4,7]])
assert finite(W)==Q
for a,b in product(range(8),repeat=2):
 x=s.Matrix([a,b])
 assert all(t.is_Integer for t in W*U*x-U*Q*x)
 assert (int((Q*x).dot(Q*x)-x.dot(x))%16)==0
result={'RQT':130,'NS_det':int(B.det()),'v1':list(v1),'v2':list(v2),
        'v1_sq':-8,'v2_sq':-8,'integral_reflections':True,
        'isometry_det':1,'target_action':Q.tolist(),'finite_checks':64,
        'W_rows':W.tolist(),'geometric_automorphism':'NOT CLAIMED',
        'Hodge_conjecture':'OPEN'}
(p/'rqt-130-results.json').write_text(json.dumps(result,indent=2))
print('PASS: 20x20 integral isometry, determinant +1, target Q on 64/64 classes')
print('STOP: geometric automorphism and ample-cone compatibility unverified')
