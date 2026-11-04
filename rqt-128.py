#!/usr/bin/env python3
"""RQT-128: enumerate all 1536 Fermat quartic monomial automorphisms.
This tests a finite subgroup of the full infinite integral orthogonal group.
Run beside the existing rqt-114.py from this repository.
"""
from itertools import product,permutations
from pathlib import Path
from collections import Counter
import sympy as S
import json
p=Path(__file__).resolve().parent
from runpy import run_path
r=run_path(str(p/'rqt-114.py'))
G,B,U,piv=r['G'],r['B'],r['U'],list(r['pivots'])
F=17
families=[((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2))]
lines=[]
for pairs in families:
 for a,b in product((1,3,5,7),repeat=2):
  eq=[]
  for (i,j),e in zip(pairs,(a,b)):
   row=[0]*4;row[i]=1;row[j]=pow(2,e,F);eq.append(row)
  lines.append(eq)
def canonical(A):
 A=[[int(v)%F for v in row] for row in A]
 rank=0
 for col in range(4):
  ix=next((j for j in range(rank,len(A)) if A[j][col]),None)
  if ix is None:continue
  A[rank],A[ix]=A[ix],A[rank]
  inv=pow(A[rank][col],-1,F)
  A[rank]=[x*inv%F for x in A[rank]]
  for j in range(len(A)):
   if j!=rank:
    t=A[j][col]
    A[j]=[(x-t*y)%F for x,y in zip(A[j],A[rank])]
  rank+=1
 return tuple(tuple(x) for x in A[:rank])
lookup={canonical(L):i for i,L in enumerate(lines)}
assert len(lookup)==48
coordinates=B.inv()*G.extract(piv,list(range(48)))
assert all(x.is_Integer for x in coordinates)
representatives={}
for a,b in product(range(8),repeat=2):
 v=U*S.Matrix([a,b])
 key=tuple(v[j]%1 for j in range(20))
 representatives[key]=(a,b)
assert len(representatives)==64
counts=Counter();examples={}
for perm in permutations(range(4)):
 for powers in product(range(4),repeat=3):
  phases=[pow(4,e,F) for e in powers]+[1]
  mapped=[]
  for L in lines:
   transformed=[]
   for row in L:
    new=[0]*4
    for j in range(4):new[perm[j]]=row[j]*pow(phases[j],-1,F)%F
    transformed.append(new)
   mapped.append(lookup[canonical(transformed)])
  assert len(set(mapped))==48
  assert all(G[i,j]==G[mapped[i],mapped[j]] for i in range(48) for j in range(48))
  W=coordinates[:,[mapped[j] for j in piv]]
  assert all(x.is_Integer for x in W)
  assert W.T*B*W==B
  assert abs(W.det(method='domain-ge'))==1
  V=W*U
  cols=[representatives[tuple(V[j,k]%1 for j in range(20))] for k in range(2)]
  Q=((cols[0][0],cols[1][0]),(cols[0][1],cols[1][1]))
  counts[Q]+=1
  examples.setdefault(Q,{'permutation':list(perm),'phase_exponents':list(powers)})
assert sum(counts.values())==1536
assert len(counts)==4 and set(counts.values())=={384}
target=((7,4),(4,7))
assert target not in counts
summary={'RQT':128,'automorphisms':1536,'all_Gram_isometries':True,'discriminant_actions':[{'Q':[list(row) for row in Q],'count':n,'example':examples[Q]} for Q,n in sorted(counts.items())],'target':[list(row) for row in target],'target_found':False,'stop':'Monomial subgroup exhausted; full integral O(NS) unsearched','general_Hodge':'OPEN'}
(p/'rqt-128-results.json').write_text(json.dumps(summary,indent=2))
print(json.dumps(summary,indent=2))
