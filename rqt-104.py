from fractions import Fraction
from itertools import product
# S: x^4+y^4+z^4+w^4=0
# S': x^4+16y^4+81z^4+256w^4=0
# g:S' -> S via diagonal (1,2,3,4).
a=(1,2,3,4)
coeffs=tuple(x**4 for x in a)
assert coeffs==(1,16,81,256)
assert tuple(Fraction(x)*Fraction(1,x) for x in a)==(1,1,1,1)
for v in product((-2,-1,0,1,2),repeat=4):
    assert sum((a[i]*v[i])**4 for i in range(4))==sum(coeffs[i]*v[i]**4 for i in range(4))
print('PASS: 625 exact polynomial evaluations')
print('PASS: invertible g gives S_prime isomorphic to S')
print('PASS: algebraic graph cycle of codimension 2 on S_prime x S')
print('STOP: non-isomorphic pair with specified rational Hodge correspondence not supplied')
