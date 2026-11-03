from fractions import Fraction as F
from itertools import product
N=22
signs=[1]*14+[-1]*8
def apply(v,which):
    if which=='plus': factors=[F(1+s,2) for s in signs]
    elif which=='minus': factors=[F(1-s,2) for s in signs]
    elif which=='quotient': factors=[F(1+s) for s in signs]
    else: raise ValueError(which)
    return tuple(a*b for a,b in zip(v,factors))
basis=[tuple(F(j==i) for j in range(N)) for i in range(N)]
zero=tuple(F(0) for _ in range(N))
for v in basis:
    p,m=apply(v,'plus'),apply(v,'minus')
    assert tuple(a+b for a,b in zip(p,m))==v
    assert apply(p,'plus')==p and apply(m,'minus')==m
    assert apply(p,'minus')==zero and apply(m,'plus')==zero
    assert apply(v,'quotient')==tuple(2*a for a in p)
assert sum(apply(v,'plus')!=zero for v in basis)==14
assert sum(apply(v,'minus')!=zero for v in basis)==8
assert sum(apply(v,'quotient')==zero for v in basis)==8
print('PASS: 22 exact basis tests; rank P+=14, rank P-=8')
print('STOP: cannot reconstruct 8 anti-invariant inputs from quotient alone')
print('HODGE CONJECTURE: OPEN')
