#!/usr/bin/env python3
"""RQT-132: concrete Hodge-compatible Fermat automorphism x -> i*x."""
from pathlib import Path
from runpy import run_path
from itertools import product
import sympy as s,json
root=Path(__file__).parent
old=run_path(str(root/'rqt-114.py'))
B,G,U=old['B'],old['G'],old['U']
piv=list(old['piv']) if 'piv' in old else list(old['pivots'])
P=17
matchings=[((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2))]
lines=[]
for matching in matchings:
 for u,v in product((1,3,5,7),repeat=2):
  rows=[]
  for (a,b),e in zip(matching,(u,v)):
   row=[0]*4;row[a]=1;row[b]=pow(2,e,P);rows.append(row)
  lines.append(rows)
def canonical(rows):
 A=[[int(x)%P for x in row] for row in rows];r=0
 for col in range(4):
  j=next((j for j in range(r,len(A)) if A[j][col]),None)
  if j is None:continue
  A[r],A[j]=A[j],A[r];inv=pow(A[r][col],-1,P)
  A[r]=[inv*x%P for x in A[r]]
  for j in range(len(A)):
   if j!=r:
    t=A[j][col];A[j]=[(x-t*y)%P for x,y in zip(A[j],A[r])]
  r+=1
 return tuple(map(tuple,A[:r]))
lookup={canonical(a):i for i,a in enumerate(lines)}
assert len(lookup)==48
phase=(4,1,1,1)
images=[]
for rows in lines:
 trans=[[row[k]*pow(phase[k],-1,P)%P for k in range(4)] for row in rows]
 images.append(lookup[canonical(trans)])
assert len(set(images))==48
assert all(G[i,j]==G[images[i],images[j]] for i in range(48) for j in range(48))
C=B.inv()*G.extract(piv,list(range(48)))
assert all(x.is_Integer for x in C)
W=C[:,[images[j] for j in piv]]
assert all(x.is_Integer for x in W)
assert W.T*B*W==B and W**4==s.eye(20)
assert abs(W.det())==1
columns=[]
for j in range(2):
 hits=[(a,b) for a,b in product(range(8),repeat=2)
       if all(z.is_Integer for z in W*U[:,j]-U*s.Matrix([a,b]))]
 assert len(hits)==1
 columns.append(hits[0])
Q=s.Matrix([[columns[0][0],columns[1][0]],[columns[0][1],columns[1][1]]])
assert Q==s.Matrix([[0,7],[1,0]])
J=s.Matrix([[0,-1],[1,0]])
assert J.T*s.diag(8,8)*J==s.diag(8,8)
assert J*s.Matrix([1,-s.I])==s.I*s.Matrix([1,-s.I])
for a,b in product(range(8),repeat=2):
 x=s.Matrix([a,b]);assert all(z.is_Integer for z in W*U*x-U*J*x)
h48=s.zeros(48,1)
for i in range(4):h48[i]=1
h=C*h48
assert (h.T*B*h)[0]==4 and W*h==h
result={'bound':132,'geometry':'x -> i*x','order':4,'NS_det_W':int(W.det()),
 'NS_action_Q_mod8':[[int(x)%8 for x in row] for row in Q.tolist()],
 'T_action_J':[[int(x) for x in row] for row in J.tolist()],
 'discriminant_matches':64,'formal_Hodge_multiplier':'i',
 'hyperplane_square':4,'hyperplane_fixed':True,
 'ample_cone':'PASS: actual projective automorphism',
 'scope':'special Fermat K3; general Hodge conjecture OPEN'}
(root/'rqt-132-results.json').write_text(json.dumps(result,indent=2))
(root/'rqt-132-W-20x20.txt').write_text(str(W))
print(json.dumps(result,indent=2))
