#!/usr/bin/env python3
"""RQT-143: six order-four generators for ambient Fermat K3 cyclic H1.
Needs rqt-142.py and its prerequisite RQT scripts in the same directory.
"""
from pathlib import Path
from runpy import run_path
from itertools import product
import sympy as s
import json
from sympy.matrices.normalforms import hermite_normal_form
p=Path(__file__).resolve().parent
old=run_path(str(p/'rqt-142.py'))
C,V,Z=old['C'],old['kernel'],old['Z']
F=hermite_normal_form(C)
assert abs(F.det())==4096
Fi=F.inv()
mod=lambda v:tuple(s.Rational(x)%1 for x in v)
def rank(bits):
 piv={}
 for a in bits:
  v=a
  while v:
   i=v.bit_length()-1
   if i in piv:v^=piv[i]
   else:piv[i]=v;break
 return len(piv)
enc=lambda v:sum((int(2*s.Rational(x))%2)<<i for i,x in enumerate(v))
selected=[];doubles=[]
for j in range(21):
 v=Fi*s.eye(21)[:,j]
 b=enc(2*v)
 if rank(doubles+[b])>len(doubles):
  selected.append(j);doubles.append(b)
assert selected==[0,1,9,10,15,19] and rank(doubles)==6
gens=[Fi*s.eye(21)[:,j] for j in selected]
assert all(all((4*x).is_Integer for x in v) and any(not (2*x).is_Integer for x in v) for v in gens)
classes=set()
for coefficients in product(range(4),repeat=6):
 v=sum((coefficients[j]*gens[j] for j in range(6)),s.zeros(21,1))
 k=mod(v)
 assert k not in classes
 classes.add(k)
assert len(classes)==4096
survivors=[]
for j in (0,2,3,4,5,6):
 u=Z[:,j+1]
 coordinates,free=V.gauss_jordan_solve(u)
 assert free.rows==0 and all(z.is_Integer for z in coordinates)
 survivors.append(mod(Fi*coordinates))
change=[]
for survivor in survivors:
 hits=[mask for mask in range(64) if mod(sum(((mask>>j&1)*2*gens[j] for j in range(6)),s.zeros(21,1)))==survivor]
 assert len(hits)==1
 change.append(hits[0])
Q=s.Matrix([[int((change[col]>>row)&1) for col in range(6)] for row in range(6)])
assert Q.det()%2==1
result={'RQT':143,'group':'(Z/4)^6','positions_0based':selected,
 'order_four_generators':6,'distinct_classes':4096,'doubles_rank_F2':6,
 'double_survivor_comparison':Q.tolist(),'comparison_det_mod2':1,
 'Hodge_conjecture':'OPEN'}
(p/'rqt-143-results.json').write_text(json.dumps(result,indent=2))
(p/'rqt-143-generators-22x6.txt').write_text(str(V[:,selected]))
print(json.dumps(result,indent=2))
