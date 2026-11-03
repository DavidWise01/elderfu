#!/usr/bin/env python3
"""RQT-112: actual 48-line Fermat quartic intersection matrix over Z.
Incidence is determined by linear equations over F17 with primitive 8th root 2.
All integer intersection numbers then follow from curve geometry.
"""
import sympy as s
from itertools import product
P=17
ZETA=2
assert pow(ZETA,4,P)==P-1 and pow(ZETA,8,P)==1
matchings=[((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2))]
lines=[]
for family,matching in enumerate(matchings):
 for u,v in product((1,3,5,7),repeat=2):
  rows=[]
  for (a,b),e in zip(matching,(u,v)):
   row=[0]*4;row[a]=1;row[b]=pow(ZETA,e,P);rows.append(row)
  lines.append((family,u,v,rows))
assert len(lines)==48
def rref(A):
 M=[row[:] for row in A];r=0
 for col in range(4):
  pivot=next((j for j in range(r,len(M)) if M[j][col]%P),None)
  if pivot is None: continue
  M[r],M[pivot]=M[pivot],M[r]
  inv=pow(M[r][col]%P,-1,P)
  M[r]=[x*inv%P for x in M[r]]
  for j in range(len(M)):
   if j!=r:
    factor=M[j][col]
    M[j]=[(x-factor*y)%P for x,y in zip(M[j],M[r])]
  r+=1
  if r==len(M):break
 return tuple(tuple(row) for row in M[:r])
def rank(A):return len(rref(A))
G=s.zeros(48)
for i in range(48):
 G[i,i]=-2
 for j in range(i+1,48):
  if rank(lines[i][3]+lines[j][3])<4:G[i,j]=G[j,i]=1
assert G==G.T
assert sum(G[i,j]==1 for i in range(48) for j in range(i+1,48))==336
assert G.rank()==20
_,pivots=G.rref()
basis=G.extract(pivots,pivots)
assert len(pivots)==20 and basis.det()==-64
lookup={rref(v[3]):i for i,v in enumerate(lines)}
ops=[((0,1,2,3),(-1,-1,1,1)),((0,1,2,3),(-1,1,-1,1)),((1,0,3,2),(1,1,1,1))]
permutations=[]
for perm,sgn in ops:
 images=[]
 for f,u,v,rows in lines:
  transformed=[]
  for row in rows:
   result=[0]*4
   for k in range(4):result[perm[k]]=row[k]*sgn[k]%P
   transformed.append(result)
  images.append(lookup[rref(transformed)])
 assert len(set(images))==48
 assert all(images[images[i]]==i for i in range(48))
 assert all(G[i,j]==G[images[i],images[j]] for i in range(48) for j in range(48))
 permutations.append(images)
A=s.eye(48)
ns_ranks=[]
for op in permutations:
 Pmat=s.eye(48)
 for j in range(48):Pmat[op[j],j]+=1
 A=A*Pmat
 ns_ranks.append((G*A).rank())
assert ns_ranks==[12,8,6]
assert [x+2 for x in ns_ranks]==[14,10,8]
print({"lines":48,"pairwise_intersections":336,"gram_rank":20,
       "chosen_basis_indices":list(pivots),"basis_determinant":-64,
       "projector_NS_ranks":ns_ranks,"projector_H2_ranks":[14,10,8],
       "status":"PASS: Fermat quartic actual line intersection pairing",
       "limit":"No general Hodge conjecture proof"})
