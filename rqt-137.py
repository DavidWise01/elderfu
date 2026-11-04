#!/usr/bin/env python3
"""RQT-137: exact glue cosets, orders, quadratic form, and lattice recovery."""
from pathlib import Path
from runpy import run_path
from itertools import product
import json
import sympy as s
from sympy.matrices.normalforms import hermite_normal_form
root=Path(__file__).resolve().parent
p=run_path(str(root/"rqt-136.py"))
Z,H=p["Z"],p["H"]
assert Z.shape==(22,22) and abs(Z.det())==512 and H.det()==-1
Zi=Z.inv();G=Z.T*H*Z
indices=[0,1,2,4,10,11,16,20]
basis=s.eye(22)
generators=[basis[:,0]]+[basis[:,j]-basis[:,0] for j in indices[1:7]]+[basis[:,20]]
def order(v):
 for k in (1,2,4):
  if all(x.is_Integer for x in Zi*(k*v)):return k
 raise AssertionError("not exponent four")
assert list(map(order,generators))==[4]+[2]*7
fractions=[Zi*v for v in generators]
def residue(v):return tuple(s.Rational(x)%1 for x in v)
classes={residue(s.zeros(22,1))}
for c,k in zip(fractions,[4]+[2]*7):
 classes={residue(s.Matrix(x)+j*c) for x in classes for j in range(k)}
assert len(classes)==512
assert all((a.T*G*b)[0].is_Integer for a in fractions for b in fractions)
assert all(((a.T*G*a)[0]/2).is_Integer for a in fractions)
Q=s.Matrix.hstack(*generators)
assert hermite_normal_form(Z.row_join(Q))==s.eye(22)
assert G.det()==-262144
output={"bound":"RQT-137","orders":[4]+[2]*7,"selected_basis_indices":indices,
"generators":["e0","e1-e0","e2-e0","e4-e0","e10-e0","e11-e0","e16-e0","e20"],
"distinct_cosets":len(classes),"quadratic_glue_isotropic":True,
"recovered_ambient_lattice":True,"ambient_Gram_determinant":int(H.det()),
"generator_22d_columns":[[int(x) for x in v] for v in generators],
"fractional_sector_coordinates":[[str(x) for x in v] for v in fractions],
"dependency":"RQT-118 and RQT-121 orientations","general_Hodge":"OPEN"}
(root/"rqt-137-results.json").write_text(json.dumps(output,indent=2))
(root/"rqt-137-glue-generators.txt").write_text(str(Q))
(root/"rqt-137-fractional-coordinates.txt").write_text(str(s.Matrix.hstack(*fractions)))
print("PASS: 8 generators, 512 cosets, integral/even glue, reconstructed full Z^22")
