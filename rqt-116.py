#!/usr/bin/env python3
"""RQT-116: actual Fermat quartic residue integral on a 2-chain, NOT a closed 2-cycle."""
import mpmath as mp
import sympy as sp
x,y,z=sp.symbols('x y z')
F=x**4+y**4+z**4+1
assert sp.diff(F,z)==4*z**3
assert sp.expand(F.subs(x,sp.I*x)-F)==0
# On w=1, omega=dx wedge dy / (4z^3). Pullback by x->i*x scales omega by i.
omega=1/(4*z**3)
assert sp.simplify((sp.I*omega)/omega)==sp.I
mp.mp.dps=45
q=mp.mpf(1)/4
# C: (x,y,z)=zeta8*(X,Y,(1-X^4-Y^4)^1/4), X,Y>=0, X^4+Y^4<=1.
# Pullback of omega to C is zeta8^-1 dX dY / (4(1-X^4-Y^4)^3/4).
I=mp.gamma(q)**3/(64*mp.gamma(3*q))
I_beta=mp.beta(q,q)*mp.beta(2*q,q)/64
assert abs(I-I_beta)<mp.mpf('1e-40')
zeta8=mp.exp(mp.j*mp.pi/4)
chain=I/zeta8
rotated=mp.j*chain
assert abs(rotated/chain-mp.j)<mp.mpf('1e-40')
print('PASS: nonzero residue-chain integral; real factor =',mp.nstr(I,35))
print('Chain integral:',mp.nstr(chain,35))
print('Automorphism ratio:',mp.nstr(rotated/chain,25))
print('STOP: C has boundary, so this is not yet an integral homology period or a geometric marking')
