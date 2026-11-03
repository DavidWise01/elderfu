#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import product
from random import Random
import json
D1=((0,-1),(1,-1),(2,1),(3,1))
D2=((0,-1),(1,1),(2,-1),(3,1))
P=((1,1),(0,1),(3,1),(2,1))
I=tuple((i,1) for i in range(4))
def mul(A,B): return tuple((B[A[i][0]][0],A[i][1]*B[A[i][0]][1]) for i in range(4))
def canon(A): return tuple((i,v*A[-1][1]) for i,v in A)
def det(A):
 p=[i for i,_ in A]; return (-1)**sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))*__import__('math').prod(v for _,v in A)
def act(A,v): return tuple(s*v[j] for j,s in A)
def f(v): return sum(x**4 for x in v)
G={canon(I)}
for bits in product(range(2),repeat=3):
 A=I
 for bit,g in zip(bits,[D1,D2,P]):
  if bit:A=mul(A,g)
 assert canon(mul(A,A))==canon(I)
 G.add(canon(A))
assert len(G)==8 and all(det(g)==1 for g in G)
assert all(canon(mul(a,b))==canon(mul(b,a)) for a in G for b in G)
for v in product(range(-2,3),repeat=4):
 for g in G:assert f(act(g,v))==f(v)
chars=list(product(range(2),repeat=3))
rank={bits:(8 if bits==(0,0,0) else 2) for bits in chars}
assert sum(rank.values())==22
for g in chars:
 trace=sum(dim*(-1)**sum(i*j for i,j in zip(g,bits)) for bits,dim in rank.items())
 assert trace==(22 if g==(0,0,0) else 6)
labels=[bits for bits in chars for _ in range(rank[bits])]
def split(v,j):
 keep=tuple(a if bits[j]==0 else F(0) for a,bits in zip(v,labels))
 side=tuple(a if bits[j]==1 else F(0) for a,bits in zip(v,labels))
 return keep,side
def pack(v):
 saved=[]
 for j in range(3):
  v,s=split(v,j);saved.append(s)
 return v,saved
def unpack(v,saved):
 for s in reversed(saved):v=tuple(a+b for a,b in zip(v,s))
 return v
rng=Random(110)
basis=[tuple(F(i==j) for j in range(22)) for i in range(22)]
mixed=[tuple(F(rng.randint(-7,7),rng.randint(1,9)) for _ in range(22)) for _ in range(128)]
assert all(unpack(*pack(v))==v for v in basis+mixed)
print(json.dumps({"kernel":"{{ i + h }}","group_order":8,"quartic_evaluations":5000,"roundtrips":150,"sector_ranks":[8]+[2]*7,"nested_core":8,"side_branches":[8,4,2],"algebraic_graphs":True,"general_Hodge":"OPEN"},indent=2))
