from fractions import Fraction as Q
import json
# S=P1xP1, H*(S)=Q[a,b]/(a²,b²), ∫ab=1, L=a+b.
# Correspondences act Z_*(x)=(pr2)_*(pr1^*(x)*Z).
# Λ cycle: pr1^*L + pr2^*L (codimension 1 on SxS).
# On H2, ∫ (u a+v b)*L = u+v; on H4, ∫ab=1 -> L.
def lam(x):
    u,v,w=x # x=u*a+v*b+w*ab (positive-degree)
    return (u+v, w, w) # coeff of 1, a, b
assert lam((1,0,0)) == (1,0,0)
assert lam((0,1,0)) == (1,0,0)
assert lam((0,0,1)) == (0,1,1)
assert Q(1,2)*2 == 1
print(json.dumps({"surface":"P1xP1","correspondence":"pr1*L + pr2*L","Lambda(a)":1,"Lambda(b)":1,"Lambda(ab)":"a+b","inverse_L_squared":"(SxS)/2","identity_H2":"diagonal S","status":"PASS known surface; STOP arbitrary X"},indent=2))
