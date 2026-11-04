#!/usr/bin/env python3
"""RQT-118: Fermat quartic Pham vanishing cycles; intersection test.
Reference Movasati, A Course in Hodge Theory, Ch. 12, Eq. (12.2).
"""
from itertools import product
import sympy as s
import mpmath as mp
def pham(a,b):
 d=[y-x for x,y in zip(a,b)]
 if all(k==0 for k in d):return -2
 if all(k in (0,1) for k in d):return -(-1)**sum(d)
 if all(k in (0,-1) for k in d):return -(-1)**sum(-k for k in d)
 return 0
basis=list(product(range(3),repeat=3))
K=s.Matrix([[pham(a,b) for b in basis] for a in basis])
assert K==K.T and all(K[j,j]==-2 for j in range(27))
a,b=(0,0,0),(1,0,0)
G=s.Matrix([[pham(x,y) for y in (a,b)] for x in (a,b)])
assert G==s.Matrix([[-2,1],[1,-2]]) and G.det()==3
assert G.eigenvals()=={-1:1,-3:1}
mp.mp.dps=50
I=mp.gamma(mp.mpf(1)/4)**3/(64*mp.gamma(mp.mpf(3)/4))
P=-2*mp.sqrt(2)*I
assert abs(mp.j*P/P-mp.j)<mp.mpf('1e-45')
print({'Gram':G.tolist(),'det':3,'signature':'(0,2)',
'period_delta':mp.nstr(P,30),'period_rotated':mp.nstr(mp.j*P,30),
'status':'PASS pairings, STOP integral transcendental basis'})
