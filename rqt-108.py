#!/usr/bin/env python3
from fractions import Fraction as Q
from random import Random
import json
N=22; signs=(1,)*14+(-1,)*8; zero=(Q(0),)*N
def p(v,s): return tuple(Q(1+s*t,2)*x for t,x in zip(signs,v))
def q(v): return tuple((1+t)*x for t,x in zip(signs,v))
def encode(v): return q(v),p(v,-1)
def decode(data):
    observation,side=data
    return tuple(a/2+b for a,b in zip(observation,side))
basis=[tuple(Q(i==j) for i in range(N)) for j in range(N)]
rng=Random(108)
mixed=[tuple(Q(rng.randint(-9,9),rng.randint(1,9)) for _ in range(N)) for _ in range(108)]
for v in basis+mixed:
    assert decode(encode(v))==v
    assert tuple(a+b for a,b in zip(p(v,1),p(v,-1)))==v
    assert p(p(v,1),-1)==zero
assert sum(q(v)==zero for v in basis)==8
assert any(decode((q(v),zero))!=v for v in basis[14:])
print(json.dumps({"roundtrips":130,"basis":22,"rational_mixed":108,"quotient_rank":14,"lost_without_side":8,"with_side":"PASS","quotient_only":"FAIL","general_Hodge":"OPEN"},indent=2))
