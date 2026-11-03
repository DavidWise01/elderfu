#!/usr/bin/env python3
"""RQT-109 exact rational nested transport; symbolic involution proxies, NOT K3 maps."""
from fractions import Fraction as F
from random import Random
import json
N=22
MASKS=(tuple(range(14,22)),tuple(range(0,5)),tuple(range(8,12)))
ZERO=(F(0),)*N
def split(v,mask):
    bad=set(mask)
    keep=tuple(F(0) if j in bad else a for j,a in enumerate(v))
    side=tuple(a if j in bad else F(0) for j,a in enumerate(v))
    return tuple(2*a for a in keep),side
def forward(v):
    sides=[]
    for mask in MASKS:
        q,s=split(v,mask)
        sides.append(s)
        v=tuple(a/2 for a in q)
    return v,sides
def backwards(base,sides):
    for side in reversed(sides):
        base=tuple(a+b for a,b in zip(base,side))
    return base
rng=Random(109)
basis=[tuple(F(i==j) for i in range(N)) for j in range(N)]
mixed=[tuple(F(rng.randint(-8,8),rng.randint(1,11)) for _ in range(N)) for _ in range(128)]
tests=basis+mixed
for v in tests:
    base,sides=forward(v)
    assert backwards(base,sides)==v
assert len(tests)==150
base,sides=forward(basis[14])
assert base==ZERO and backwards(base,[ZERO]*3)!=basis[14]
base,sides=forward(basis[1])
assert backwards(base,[sides[0],ZERO,sides[2]])!=basis[1]
print(json.dumps({"kernel":"{{ i + h }}","roundtrips":150,"passed":150,"dimension":22,"stages":3,"first_stage_ranks":[14,8],"missing_branch":"FAIL","real_algebraic_K3_maps_for_stages_2_3":"NOT PROVIDED / STOP","Hodge_conjecture":"OPEN"},indent=2))
