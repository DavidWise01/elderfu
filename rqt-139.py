#!/usr/bin/env python3
"""RQT-139 fixed glue subgroup versus pointwise fixed integral cycles."""
from pathlib import Path
from itertools import product
from runpy import run_path
import sympy as s,json
root=Path(__file__).resolve().parent
r=run_path(str(root/"rqt-137.py"))
t=run_path(str(root/"rqt-133.py"))
Z,H,X=r["Z"],r["H"],t["X"]
E=s.Matrix.hstack(*r["gens"])
assert Z.shape==H.shape==X.shape==(22,22) and E.shape==(22,8)
assert abs(Z.det())==512 and X**4==s.eye(22) and H.det()==-1
Zi=Z.inv();A=Zi*X*Z
assert all(x.is_Integer for x in A)
V=[Zi*E[:,j] for j in range(8)]
def residue(v):return tuple(s.Rational(x)%1 for x in v)
labels=[]
for a in (0,2):
 for bits in product((0,1),repeat=7):
  v=sum((((a,)+bits)[j]*V[j] for j in range(8)),s.zeros(22,1))
  assert residue(A*v)==residue(v)
  assert residue(2*v)==(s.Integer(0),)*22
  labels.append(residue(v))
assert len(set(labels))==256
G=Z.T*H*Z
assert all((v.T*G*w)[0].is_Integer for v in V for w in V)
assert all(((v.T*G*v)[0]/2).is_Integer for v in V)
fixed_gen=s.Matrix.hstack(2*E[:,0],*[E[:,j] for j in range(1,8)])
assert len({residue(Zi*fixed_gen*s.Matrix(b)) for b in product((0,1),repeat=8)})==256
fixed=Z[:,0]
assert X*fixed==fixed and (fixed.T*H*fixed)[0]==4
assert (X-s.eye(22)).rank()==21
# Any X-fixed integral representative lies in ker_Z(X-I)=Z*e0, hence
# maps to the zero class in ambient / primitive sector sum.
assert Zi*fixed==s.eye(22)[:,0]
result={"RQT":139,"fixed_glue_count":256,"fixed_group":"(Z/2)^8",
"fixed_glue_generators":["2g0","g1","g2","g3","g4","g5","g6","g7"],
"all_fixed_group_elements_exponent_two":True,
"glue_bilinear_mod_integers":"zero",
"glue_quadratic_mod_two":"zero",
"fixed_integral_lattice_rank":1,
"fixed_integral_primitive_generator":[int(v) for v in fixed],
"fixed_generator_square":4,
"fixed_cosets_with_pointwise_fixed_integral_lift":1,
"fixed_cosets_without_pointwise_fixed_integral_lift":255,
"caveat":"Fixed mod the primitive sector lattice does not imply pointwise fixed.",
"dependency":"RQT-118/121 Pham orientations","general_Hodge":"OPEN"}
(root/"rqt-139-results.json").write_text(json.dumps(result,indent=2))
(root/"rqt-139-fixed-glue-generators.txt").write_text(str(fixed_gen))
print(json.dumps(result,indent=2))
