#!/usr/bin/env python3
"""RQT-141: exact six complementary cohomology classes."""
from pathlib import Path
from runpy import run_path
from itertools import product
import sympy as s,json
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
p=Path(__file__).resolve().parent
b=run_path(str(p/'rqt-136.py'))
q=run_path(str(p/'rqt-133.py'))
f=run_path(str(p/'rqt-139.py'))
Z,X,E=b['Z'],q['X'],f['fixed_gen']
A=Z.inv()*X*Z;I=s.eye(22)
N=I+A+A**2+A**3
assert N==s.diag(4,*([0]*21))
K=(A-I)[1:,1:]
D=smith_normal_form(K,domain=ZZ)
assert [abs(int(D[i,i])) for i in range(21)]==[1]*7+[2]*14
Ki=K.inv()
assert all((2*v).is_Integer for v in Ki)
B=Ki*(Z.inv()*(X-I)*E)[1:,:]
def bits(v):
 return sum((int((2*s.Rational(z))%2)<<i) for i,z in enumerate(v))
def rank(seq):
 piv={}
 for x in seq:
  v=x
  while v:
   i=v.bit_length()-1
   if i in piv:v^=piv[i]
   else:piv[i]=v;break
 return len(piv)
image=[bits(B[:,i]) for i in range(8)]
assert rank(image)==8
candidates=[bits(Ki[:,i]) for i in range(21)]
assert rank(candidates)==14
chosen=[];total=list(image)
for j,c in enumerate(candidates):
 if rank(total+[c])>len(total):
  chosen.append(j);total.append(c)
assert chosen==[0,2,3,4,5,6] and rank(total)==14
for mask in range(64):
 v=0
 for i in range(6):
  if mask>>i&1:v^=candidates[chosen[i]]
 assert rank(image+[v])==8+(mask!=0)
for j in chosen:
 d=s.eye(21)[:,j]
 assert N*s.Matrix.vstack(s.zeros(1,1),d)==s.zeros(22,1)
 assert all(t.is_Integer for t in 2*Ki*d)
out={'RQT':141,'H1':'(Z/2)^14','image':'(Z/2)^8',
 'chosen_complement':'(Z/2)^6','cocycle_indices_0based':chosen,
 'cocycle_indices_in_22D':[j+1 for j in chosen],
 'F2_rank_total':14,'scope':'conditional Fermat K3; Hodge OPEN'}
(p/'rqt-141-results.json').write_text(json.dumps(out,indent=2))
print(out)
