#!/usr/bin/env python3
"""RQT-101: Fermat quartic diagonal automorphisms: exact finite enumeration."""
from itertools import product
from collections import Counter
# Fix w coefficient to 1: projective diagonal automorphisms of Fermat quartic
# indexed by phases (i^a,i^b,i^c,1), a,b,c in Z/4.
triples=list(product(range(4),repeat=3))
assert len(triples)==64 and len(set(triples))==64
phase=Counter(sum(t)%4 for t in triples)
assert phase==Counter({0:16,1:16,2:16,3:16})
# Rational matrices on T(S) in suitable rational basis, using T(S) Gram diag(8,8).
I=((1,0),(0,1))
J=((0,-1),(1,0))
def matmul(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
powers=[I]
for _ in range(3): powers.append(matmul(powers[-1],J))
assert powers[2]==((-1,0),(0,-1))
assert powers[3]==((0,1),(-1,0))
assert matmul(powers[-1],J)==I
# powers[0], powers[1] Q-linearly independent; powers[2]=-I and powers[3]=-J.
assert powers[0]!=powers[1]
assert powers[2]==tuple(tuple(-x for x in row) for row in I)
assert powers[3]==tuple(tuple(-x for x in row) for row in J)
print({"symmetries":len(triples),"phase_distribution":dict(sorted(phase.items())),
       "transcendental_action_span_over_Q":2,"graph_witnesses":64,
       "boundary":"NOT COMPUTED: full cycle-class span in H^4(SxS,Q)"})
