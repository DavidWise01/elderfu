#!/usr/bin/env python3
"""RQT-122: integral K3 lattice basis from 20 Fermat lines and two closed Pham cycles.
Imports geometric intersection data from RQT-121. All checks exact.
"""
import runpy, sympy as s, json
from pathlib import Path
root=Path(__file__).resolve().parent
D=runpy.run_path(str(root/"rqt-121.py"))
G=D["G"]; piv=D["piv"]; B=D["B"]; d=D["d"]; r=D["r"]
assert len(piv)==20 and B.det()==-64
A=s.Matrix([[-2,1],[1,-2]])
C=s.Matrix.hstack(d,r)
H=B.row_join(C).col_join(C.T.row_join(A))
assert H.shape==(22,22) and H==H.T
assert all(x.is_Integer for x in H)
assert all((H[j,j]/2).is_Integer for j in range(22))
assert H.det()==-1, H.det()
T=s.simplify(A-C.T*B.inv()*C)
assert T==s.diag(s.Rational(1,8),s.Rational(1,8))
assert H.rank()==22
result={
 "rank":22,"determinant":-1,"even":True,"integral":True,
 "known_NS_signature":[1,19],
 "transcendental_Schur_complement":[["1/8","0"],["0","1/8"]],
 "full_signature":[3,19],
 "line_basis_indices_0based":list(piv),
 "cycle_pairings":{"Delta":[int(x) for x in d],"gxDelta":[int(x) for x in r]},
 "conditional_geometric_integral_basis":True,
 "dependencies":"RQT-121 signed local intersections, RQT-118 raw Pham intersection",
 "general_Hodge":"OPEN"
}
(root/"rqt-122-results.json").write_text(json.dumps(result,indent=2))
(root/"rqt-122-gram.txt").write_text(str(H))
print(json.dumps(result,indent=2))
