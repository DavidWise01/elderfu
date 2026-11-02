from fractions import Fraction as F
import json
# An abstract two-component rational subspace of H²(S,Q) for quartic K3 S.
# h²=4; v.h=0; x=a*h+b*v. This is a restricted test,
# not a computation of the entire 22-dimensional K3 cohomology lattice.
def project(a,b):
    xh=4*a
    return (a-xh/F(4),b)
cases=[(F(1),F(0)),(F(0),F(1)),(F(3),F(5,7)),(F(-2,3),F(9,11))]
data=[]
for a,b in cases:
    y=project(a,b); yy=project(*y)
    assert y==(F(0),b) and yy==y
    data.append({"input":[str(a),str(b)],"projected":[str(t) for t in y],"idempotent":yy==y})
result={"variety":"smooth quartic K3 S (assumed)","polarization":"h^2=4",
"cycle":"[Delta_S]-(1/4)*pr1^*h*pr2^*h",
"cohomological_action":"x -> x-(x.h/4)h on H^2(S,Q)",
"tests":data,"status":"PASS on polarization/primitive split",
"stop":"No cycle constructed for arbitrary rational (2,2) Hodge class on S x S",
"scope":"This primitive projector is algebraic; it does not prove Hodge for S x S"}
print(json.dumps(result,indent=2))
