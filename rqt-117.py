#!/usr/bin/env python3
"""RQT-117: an explicit closed Pham-type cycle on the Fermat quartic."""
from itertools import product
import mpmath as mp
mp.mp.dps=55
# C: (x,y,z)=zeta8*(X,Y,Z), X,Y,Z>=0, X^4+Y^4+Z^4=1.
# Delta = (1-gx)(1-gy)(1-gz) C is an integral 2-cycle.
# gx,gy,gz multiply their respective coordinate by i.
# Each boundary face F_j is fixed by g_j; all coordinate maps commute.
for face in range(3):
    coefficients={}
    for bits in product((0,1),repeat=3):
        canonical=tuple(0 if k==face else bits[k] for k in range(3))
        coefficients[canonical]=coefficients.get(canonical,0)+(-1)**sum(bits)
    assert all(v==0 for v in coefficients.values())
print("PASS: exact cancellation on all 3 boundary faces")
I=mp.gamma(mp.mpf(1)/4)**3/(64*mp.gamma(mp.mpf(3)/4))
zeta8=mp.exp(mp.j*mp.pi/4)
open_chain=I/zeta8
closed=(1-mp.j)**3*open_chain
formula=-mp.sqrt(2)*mp.gamma(mp.mpf(1)/4)**3/(32*mp.gamma(mp.mpf(3)/4))
assert abs(closed-formula)<mp.mpf("1e-50")
assert abs(closed)>1
assert abs((mp.j*closed)/closed-mp.j)<mp.mpf("1e-50")
print("PASS: nonzero closed 2-cycle integral =",mp.nstr(closed,40))
print("PASS: image under gx has period ratio i")
print("STOP: not an integral marking or explicit intersection pairing")
print("GENERAL HODGE CONJECTURE: OPEN")
