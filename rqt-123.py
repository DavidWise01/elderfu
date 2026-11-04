#!/usr/bin/env python3
"""RQT-123: independent numerical real-Jacobian vertex-sign audit and gluing comparison.
Requires rqt-121.py and rqt-114.py in the same GitHub directory.
"""
from itertools import product
from pathlib import Path
from math import pi,cos,sin
import numpy as np
import sympy as s
import runpy,json
root=Path(__file__).resolve().parent
old=runpy.run_path(str(root/"rqt-121.py"))
lines=old["lines"]; D=old["D"]; R=old["R"]
z=complex(cos(pi/4),sin(pi/4))
def independent_count(line,offset,eps):
 j,ew,(a,b),e=line
 lam=-z**e; total=0
 for bits in product((0,1),repeat=3):
  k=[bits[i]+offset[i] for i in range(3)]
  if (1+2*k[j]-ew-4)%8:continue
  A=z**(1+2*k[a]); C=z**(1+2*k[b])
  # Solve complex affine line u-lambda*v=epsilon against oriented real cone.
  matrix=np.array([[A.real,(-lam*C).real],[A.imag,(-lam*C).imag]])
  v=np.linalg.solve(matrix,np.array([eps.real,eps.imag]))
  if min(v)<0:continue
  # Independent REAL tangent-frame Jacobian (Re u,Im u,Re v,Im v).
  jac=np.array([[A.real,0,lam.real,-lam.imag],
                [A.imag,0,lam.imag,lam.real],
                [0,C.real,1,0],
                [0,C.imag,0,1.]])
  delta=np.linalg.det(jac)
  assert abs(delta)>0.3
  total+=(-1)**(sum(bits)+j)*int(np.sign(delta))
 return total
angles=[0.19,0.53,1.12,1.88,2.41,3.33,4.56,5.72]
for angle in angles:
 eps=.091*complex(cos(angle),sin(angle))
 assert [independent_count(L,(0,0,0),eps) for L in lines]==D
 assert [independent_count(L,(1,0,0),eps) for L in lines]==R
G=old["G"]; piv=old["piv"]; B=G.extract(piv,piv)
d=s.Matrix([D[i] for i in piv]); r=s.Matrix([R[i] for i in piv])
C=s.Matrix.hstack(d,r); A=s.Matrix([[-2,1],[1,-2]])
H=B.row_join(C).col_join(C.T.row_join(A))
S=s.simplify(A-C.T*B.inv()*C)
assert S==s.diag(s.Rational(1,8),s.Rational(1,8))
assert H.det()==-1 and all(H[j,j]/2 in s.ZZ for j in range(22))
# Independent comparison with RQT-114's specific chosen discriminant gluing:
abstract=runpy.run_path(str(root/"rqt-114.py"))
U=abstract["U"]
DU=B.inv()*C
solutions=[]
for perm in [(0,1),(1,0)]:
 for signs in product((-1,1),repeat=2):
  Q=s.zeros(2)
  for k in range(2):Q[perm[k],k]=signs[k]
  if all(x in s.ZZ for x in DU-U*Q):
   solutions.append(str(Q))
assert len(solutions)==0
result={
 "independent_method":"direct 4x4 real tangent Jacobian and 2x2 numeric intersection solve",
 "perturbations":8,"line_sign_checks":768,
 "all_RQT121_signs_match":True,"full_Gram_determinant":-1,
 "even_integral":True,"transcendental_Schur":"diag(1/8,1/8)",
 "RQT114_NS_fixed_isometry_matches":0,
 "first_stop":"A non-NS-fixed isometry or geometric identification remains unconstructed",
 "Pham_raw_cycle_Gram":"imported from RQT-118, not rederived",
 "Hodge_conjecture":"OPEN"
}
(root/"rqt-123-results.json").write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
