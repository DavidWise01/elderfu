#!/usr/bin/env python3
"""RQT-105 — Fermat K3 to non-isomorphic Kummer K3 via Nikulin involution.
The integral transcendental lattices are published theorem inputs.
"""
from itertools import product
import json
def invol(v):
    x,y,z,w=v
    return (x,y,-z,-w)
def quartic(v): return sum(n**4 for n in v)
def quotient(v):
    x,y,z,w=v
    return (x,y,z*z,w*w,z*w)
def relations(q):
    x,y,A,B,C=q
    return x**4+y**4+A*A+B*B,C*C-A*B
n=0
for v in product((-2,-1,0,1,2),repeat=4):
    assert invol(invol(v))==v
    assert quartic(invol(v))==quartic(v)
    assert quotient(invol(v))==quotient(v)
    f,g=relations(quotient(v))
    assert f==quartic(v) and g==0
    n+=1
assert n==625
TS=((8,0),(0,8));TY=((4,0),(0,4))
det=lambda M:M[0][0]*M[1][1]-M[0][1]*M[1][0]
assert det(TS)==64 and det(TY)==16
assert all(TS[i][j]==2*TY[i][j] for i in range(2) for j in range(2))
print(json.dumps({
 "kernel":"{{ i + h }}",
 "exact_tuples_checked":n,
 "fixed_points_over_C":8,
 "transcendental_discriminants":[64,16],
 "lattice_relation":"T(Y)(2)=T(S), published result",
 "nonisomorphic":"PASS from published integral lattices",
 "correspondence":"closure of graph of rational quotient-to-resolution map",
 "Hodge_similarity_multiplier":2,
 "general_arbitrary_pair":"STOP: no universal algebraic-cycle construction",
 "general_Hodge_conjecture":"OPEN"},indent=2))
