from fractions import Fraction as F
from itertools import product
from random import Random
chars=list(product((0,1),repeat=3))
labels=[c for c in chars for _ in range(8 if c==(0,0,0) else 2)]
assert len(labels)==22
gram=[F(1) if i<3 else F(-1) for i in range(22)]
def inner(u,v):return sum(gram[i]*u[i]*v[i] for i in range(22))
def split(v,k):
 return (tuple(a if c[k]==0 else F(0) for a,c in zip(v,labels)),tuple(a if c[k]==1 else F(0) for a,c in zip(v,labels)))
def action(v,g):return tuple(((-1)**sum(a*b for a,b in zip(c,g)))*x for x,c in zip(v,labels))
def encode(v):
 sides=[]
 for k in range(3):
  v,s=split(v,k);sides.append(s)
 return v,sides
def decode(v,sides):
 for s in reversed(sides):v=tuple(a+b for a,b in zip(v,s))
 return v
rng=Random(111)
basis=[tuple(F(i==j) for j in range(22)) for i in range(22)]
mixed=[tuple(F(rng.randint(-5,5),rng.randint(1,7)) for _ in range(22)) for _ in range(128)]
test=basis+mixed
for v in test:
 core,sides=encode(v);parts=[core]+sides
 assert decode(core,sides)==v
 assert all(inner(a,b)==0 for i,a in enumerate(parts) for j,b in enumerate(parts) if i!=j)
 assert inner(v,v)==sum(inner(x,x) for x in parts)
 assert all(inner(action(v,g),action(v,g))==inner(v,v) for g in chars)
for v,w in zip(test[::2],test[1::2]):
 assert all(inner(action(v,g),action(w,g))==inner(v,w) for g in chars)
assert sum(x>0 for x in gram)==3 and sum(x<0 for x in gram)==19
print('PASS: 150 exact rational roundtrips, orthogonality, and 8 group isometries')
print('SIGNATURES: (3,5), (0,8), (0,4), (0,2)')
print('STOP: actual integral K3 Gram lattice not constructed')
