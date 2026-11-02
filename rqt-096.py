from fractions import Fraction as F
import json
# S = CP1 x CP1; H*=Q[a,b]/(a²,b²), ∫ab=1
# L=a+b, L²=2ab; inverse of H0 -> H4 is algebraic correspondence
# Z=(1/2)[S x S] codimension zero, acting H4 -> H0 by pushforward.
forward_coefficient=F(2)
correspondence=F(1,2)
samples=[F(-5,3),F(0),F(7,11)]
assert all(correspondence*(forward_coefficient*x)==x for x in samples)
print(json.dumps({"space":"CP1 x CP1","L_squared":"2ab","correspondence":"1/2 [S x S]","samples":[str(x) for x in samples],"pass":True,"general_case":"STOP at missing universal algebraic correspondence"},indent=2))
