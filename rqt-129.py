#!/usr/bin/env python3
"""RQT-129: exact 48 Fermat root reflections and full finite discriminant group."""
from pathlib import Path
import runpy,itertools,json
import sympy as s
p=Path(__file__).resolve().parent
r=runpy.run_path(str(p/"rqt-114.py"))
B,G,piv,U=r["B"],r["G"],list(r["pivots"]),r["U"]
assert B.det()==-64
coords=B.inv()*G.extract(piv,list(range(48)))
assert all(x.is_Integer for x in coords)
identity=s.eye(20)
for j in range(48):
 v=coords[:,j]
 assert (v.T*B*v)[0]==-2
 W=identity+v*(v.T*B)
 assert W.T*B*W==B and W*W==identity
 assert W.det(method="domain-ge")==-1
 assert all(x.is_Integer for x in W*U-U)
finite=[]
for a,b,c,d in itertools.product(range(8),repeat=4):
 if (a*a+c*c-1)%16 or (b*b+d*d-1)%16 or (a*b+c*d)%8:continue
 if (a*d-b*c)%2==0:continue
 Q=((a,b),(c,d))
 for x,y in itertools.product(range(8),repeat=2):
  xx=(a*x+b*y)%8;yy=(c*x+d*y)%8
  assert (xx*xx+yy*yy-x*x-y*y)%16==0
 finite.append(Q)
assert len(finite)==16
monomial=[((1,0),(0,1)),((7,0),(0,7)),((0,1),(7,0)),((0,7),(1,0))]
assert all(q in finite for q in monomial)
target=((7,4),(4,7))
assert target in finite and target not in monomial
assert (s.Matrix(target)**2).applyfunc(lambda x:int(x)%8)==s.eye(2)
result={"RQT":129,"line_reflections":48,"all_reflections_isometries":True,
"all_reflections_identity_on_discriminant":True,
"finite_form_group_size":16,"monomial_image_size":4,
"target":[list(row) for row in target],"target_in_full_finite_group":True,
"target_in_monomial_plus_root_reflection_image":False,
"full_integral_lift_in_line_basis":"NOT CONSTRUCTED",
"general_Hodge_conjecture":"OPEN"}
(p/"rqt-129-results.json").write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
