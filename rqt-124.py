#!/usr/bin/env python3
"""RQT-124: exact discriminant transition and integral lift in standard NS model.
Requires repository rqt-114.py and rqt-121.py; not a geometric line-basis isometry.
"""
import runpy,itertools,json
from pathlib import Path
import sympy as s
root=Path(__file__).resolve().parent
a=runpy.run_path(str(root/"rqt-114.py"))
b=runpy.run_path(str(root/"rqt-121.py"))
B=a["B"];U=a["U"];piv=a["pivots"]
assert piv==b["piv"]
D=s.Matrix.hstack(s.Matrix([b["D"][i] for i in piv]),s.Matrix([b["R"][i] for i in piv]))
V=B.inv()*D
frac=lambda x:s.Rational(x)-s.floor(x)
columns=[]
for j in range(2):
 sols=[(u,v) for u,v in itertools.product(range(8),repeat=2)
       if all(frac(V[i,j]-u*U[i,0]-v*U[i,1])==0 for i in range(20))]
 assert len(sols)==1
 columns.append(s.Matrix(sols[0]))
Q=s.Matrix.hstack(*columns)
assert Q==s.Matrix([[7,4],[4,7]]) and Q.det()%8==1
assert all(frac(V[i,j]-(U*Q)[i,j])==0 for i in range(20) for j in range(2))
K=s.Matrix([[0,1,0,0],[1,0,0,0],[0,0,-8,0],[0,0,0,-8]])
M=s.Matrix([[4,13,24,16],[5,16,32,16],[1,4,7,4],[2,6,12,7]])
assert M.det()==-1 and M.T*K*M==K
assert all((M[i+2,j+2]-Q[i,j])%8==0 for i in range(2) for j in range(2))
assert all(M[i,j+2]%8==0 for i in range(2) for j in range(2))
classes=set()
for u,v in itertools.product(range(8),repeat=2):
 x=s.Matrix([u,v]);y=Q*x
 assert (int(y.dot(y)-x.dot(x))%16)==0
 classes.add(tuple(int(z)%8 for z in y))
assert len(classes)==64
result={"status":"PASS: explicit integral discriminant lift","discriminant_matrix_mod_8":Q.tolist(),
"standard_factor_Gram":K.tolist(),"integral_4x4_lift":M.tolist(),
"lift_determinant":-1,"finite_form_checks":64,
"standard_NS_extension":"M direct_sum identity on E8(-1)^2",
"line_to_standard_basis":"NOT COMPUTED / STOP","general_Hodge_conjecture":"OPEN"}
result={k:( [[int(v) for v in row] for row in x] if isinstance(x,list) and x and isinstance(x[0],list) else x) for k,x in result.items()}
(root/"rqt-124-results.json").write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
