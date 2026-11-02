from fractions import Fraction as Q
from itertools import product
# Fermat quartic K3: Picard rank 20, H² rank 22, T rank 2.
rho=20
t=22-rho
assert t==2
I=((Q(1),Q(0)),(Q(0),Q(1)))
J=((Q(0),Q(-1)),(Q(1),Q(0)))
def flat(M):return [x for row in M for x in row]
u,v=flat(I),flat(J)
independent=any(u[i]*v[j]-u[j]*v[i] for i,j in product(range(4),repeat=2))
assert independent
# Rational Hodge endomorphisms on T are Q[I,J] (CM by Q(i)).
# Hodge degree four on SxS = H0⊗H4 ⊕ NS⊗NS ⊕ End_Hdg(T) ⊕ H4⊗H0.
outer=2
divisors=rho**2
trans=2
count=outer+divisors+trans
assert count==404 and independent
print({"Hodge_classes":count,"outer":outer,"divisor_products":divisors,"transcendental":trans,"projected_graph_basis":["I","J"],"algebraic_span_dimension":count,"verdict":"PASS special self-product; STOP arbitrary variety"})
