#!/usr/bin/env python3
from fractions import Fraction as Q
from itertools import product
# Compatible-base *model* on transcendental rational cohomology,
# not an independent computed period-basis action.
TX=((8,0),(0,8)); TY=((4,0),(0,4))
I=((Q(1),Q(0)),(Q(0),Q(1)))
PULL=I
PUSH=((Q(2),Q(0)),(Q(0),Q(2)))
def mm(a,b): return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def mv(a,v): return tuple(sum(a[i][j]*v[j] for j in range(2)) for i in range(2))
def f(g,v): return sum(Q(g[i][j])*v[i]*v[j] for i in range(2) for j in range(2))
HALFPULL=tuple(tuple(x/2 for x in row) for row in PULL)
HALFPUSH=tuple(tuple(x/2 for x in row) for row in PUSH)
assert mm(PULL,PUSH)==((2,0),(0,2))
assert mm(PUSH,PULL)==((2,0),(0,2))
n=0
for v in product(range(-2,3),repeat=2):
 v=tuple(map(Q,v))
 assert mv(HALFPULL,mv(PUSH,v))==v
 assert mv(HALFPUSH,mv(PULL,v))==v
 assert f(TY,mv(PUSH,v))==2*f(TX,v)
 assert f(TX,mv(PULL,v))==2*f(TY,v)
 n+=1
assert n==25
print('PASS:',n,'transcendental rational test vectors')
print('STOP: q* q_* = 1 + involution is zero on anti-invariant divisors, not 2I on all H2')
print('GENERAL HODGE CONJECTURE: OPEN')
