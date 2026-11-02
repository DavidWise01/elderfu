#!/usr/bin/env python3
# RQT-100: concrete Fermat quartic automorphism (exact arithmetic)
import sympy as s
x,y,z,w=s.symbols('x y z w')
F=x**4+y**4+z**4+w**4
A=s.diag(s.I,1,1,1)
assert s.expand(F.subs(x,s.I*x)-F)==0
assert A**4==s.eye(4)
assert s.det(A)==s.I
assert s.simplify(s.det(A)**4)==1
print('PASS: quartic preserved, order four, determinant i')
print('CERTIFICATE: graph of a projective algebraic automorphism of Fermat K3')
print('STOP: no argument generating arbitrary rational Hodge cycles')
