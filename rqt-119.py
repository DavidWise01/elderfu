#!/usr/bin/env python3
from itertools import product
import sympy as s
from pathlib import Path
import json
MATCH=[((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2))]
lines=[]
for f,pairs in enumerate(MATCH):
 for u,v in product((1,3,5,7),repeat=2):
  wp=next(p for p in pairs if 3 in p)
  j=next(x for x in wp if x!=3)
  e=u if wp==pairs[0] else v
  rows=[]
  for (a,b),phase in zip(pairs,(u,v)):
   r=[0]*4;r[a]=1;r[b]=pow(2,phase,17);rows.append(r)
  lines.append((f,u,v,j,e,rows))
def contacts(line,shift):
 j,e=line[3:5]
 return sum((1+2*(mask[j]+shift[j])-e-4)%8==0 for mask in product((0,1),repeat=3))
def rank17(rows):
 A=[[x%17 for x in row] for row in rows];r=0
 for col in range(4):
  q=next((i for i in range(r,len(A)) if A[i][col]),None)
  if q is None:continue
  A[r],A[q]=A[q],A[r];inv=pow(A[r][col],-1,17)
  A[r]=[x*inv%17 for x in A[r]]
  for i in range(len(A)):
   if i!=r:
    z=A[i][col];A[i]=[(a-z*b)%17 for a,b in zip(A[i],A[r])]
  r+=1
  if r==len(A):break
 return r
G=s.zeros(48)
for i in range(48):
 G[i,i]=-2
 for j in range(i+1,48):
  G[i,j]=G[j,i]=int(rank17(lines[i][-1]+lines[j][-1])<4)
assert G.rank()==20
zeroD=[i for i,L in enumerate(lines) if contacts(L,(0,0,0))==0]
zeroR=[i for i,L in enumerate(lines) if contacts(L,(1,0,0))==0]
common=sorted(set(zeroD)&set(zeroR))
assert len(zeroD)==len(zeroR)==24 and len(common)==20
assert (G[:,zeroD].rank(),G[:,zeroR].rank(),G[:,common].rank())==(18,18,16)
assert sum(contacts(L,(0,0,0)) for L in lines)==96
assert sum(contacts(L,(1,0,0)) for L in lines)==96
result={"fermat_lines":48,"NS_rank":20,"disjoint_lines_per_cycle":[24,24],"common_disjoint_lines":20,"independent_zero_constraints":[18,18],"common_constraint_rank":16,"remaining_NS_unknown_dimensions":[2,2],"common_disjoint_indices_zero_based":common,"local_vertex_intersection_numbers":"NOT COMPUTED","transcendental_projection":"STOP","general_Hodge":"OPEN"}
print(json.dumps(result,indent=2))
if __name__=="__main__":Path(__file__).with_name("results.json").write_text(json.dumps(result,indent=2))
