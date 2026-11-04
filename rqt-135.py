#!/usr/bin/env python3
"""RQT-135: rational four-tick projector decomposition of Fermat H2."""
from pathlib import Path
from runpy import run_path
import sympy as s
import json
root=Path(__file__).resolve().parent
old=run_path(str(root/"rqt-133.py"))
X,H=old["X"],old["H"]
I=s.eye(22)
assert X**4==I and X.T*H*X==H
Pp=(I+X+X**2+X**3)/4
Pm=(I-X+X**2-X**3)/4
Pr=(I-X**2)/2
P={"fixed_plus":Pp,"reversed_minus":Pm,"quarter_turn":Pr}
assert sum(P.values(),s.zeros(22))==I
assert all(A*A==A for A in P.values())
assert all(A*B==s.zeros(22) for ka,A in P.items() for kb,B in P.items() if ka!=kb)
assert all(A.T*H*B==s.zeros(22) for ka,A in P.items() for kb,B in P.items() if ka!=kb)
assert X*Pp==Pp and X*Pm==-Pm and X**2*Pr==-Pr
ranks={k:int(A.rank()) for k,A in P.items()}
assert ranks=={"fixed_plus":1,"reversed_minus":7,"quarter_turn":14}
assert s.factor(X.charpoly().as_expr())==(s.Symbol("lambda")-1)*(s.Symbol("lambda")+1)**7*(s.Symbol("lambda")**2+1)**7
den={k:next(d for d in (1,2,4) if all(v.is_Integer for v in d*A)) for k,A in P.items()}
assert den=={"fixed_plus":4,"reversed_minus":4,"quarter_turn":2}
cols={k:[j for j in range(22) if all(v.is_Integer for v in A[:,j])] for k,A in P.items()}
assert list(map(len,cols.values()))==[2,0,0]
delta=s.eye(22)[:,20]
parts=[A*delta for A in P.values()]
assert sum(parts,s.zeros(22,1))==delta
result={"RQT":135,"ranks":ranks,"characteristic_polynomial":"(t-1)(t+1)^7(t^2+1)^7",
"rational_orthogonal_projectors":True,"clearing_denominators":den,
"integral_columns":cols,
"delta_projected_components":[[str(v) for v in c] for c in parts],
"integral_direct_sum":"NOT ESTABLISHED",
"dependency":"RQT-118/121 Pham orientations",
"general_Hodge_conjecture":"OPEN"}
(root/"rqt-135-results.json").write_text(json.dumps(result,indent=2))
for k,A in P.items():(root/(k+"-projector.txt")).write_text(str(A))
print(json.dumps({k:v for k,v in result.items() if k!="delta_projected_components"},indent=2))
