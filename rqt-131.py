#!/usr/bin/env python3
"""RQT-131 — strict integral gluing gate for RQT-130 Fermat NS isometry."""
from pathlib import Path
from itertools import product,permutations
from runpy import run_path
import sympy as s,json
root=Path(__file__).resolve().parent
prior=run_path(str(root/'rqt-130.py'))
W,Q,B,U=prior['W'],prior['Q'],prior['B'],prior['U']
T=s.diag(8,8)
isometries=[]
for perm in permutations(range(2)):
 for signs in product((-1,1),repeat=2):
  J=s.zeros(2)
  for i in range(2):J[perm[i],i]=signs[i]
  assert J.T*T*J==T
  isometries.append(J)
assert len(isometries)==8
compatible=[J for J in isometries if all((J[i,j]-Q[i,j])%8==0 for i in range(2) for j in range(2))]
assert Q==s.Matrix([[7,4],[4,7]]) and not compatible
G=prior['prior']['G']; piv=list(prior['prior']['pivots'])
h48=s.zeros(48,1)
for i in range(4):h48[i]=1
h=B.inv()*G.extract(piv,list(range(48)))*h48
assert all(z.is_Integer for z in h)
assert (h.T*B*h)[0]==4
assert (W*h).T*B*(W*h)==s.Matrix([[4]])
assert (h.T*B*W*h)[0]==220
result={'bound':131,'transcendental_gram':T.tolist(),
'integral_transcendental_isometries':8,'gluing_matches':0,
'NS_discriminant_action':Q.tolist(),'integral_H2_extension':'FAIL',
'h_square':4,'W_h_square':4,'h_dot_W_h':220,
'status':'STOP: no integral T-isometry realizes Q; no geometric automorphism from this W',
'Hodge_conjecture':'OPEN'}
(root/'rqt-131-results.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
