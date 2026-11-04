#!/usr/bin/env python3
"""RQT-126 exact norm-2 roots of the RQT-125 negative-definite complement.
The floating Cholesky is ONLY for choosing a unimodular reduced basis;
the enumeration and root completeness checks use exact SymPy rationals.
"""
from pathlib import Path
import runpy,json
from math import isqrt
import numpy as np
import sympy as s
root=Path(__file__).resolve().parent
prior=runpy.run_path(str(root/'rqt-125.py'))
N=prior['N']
assert N.shape==(18,18) and N.det()==64 and N==N.T
A=-N
assert all(A[:k,:k].det()>0 for k in range(1,19))
L=np.linalg.cholesky(np.array(A.tolist(),dtype=float)).T
embedding=s.Matrix(np.rint(L*10000).astype('int64').tolist()).T
_,T=embedding.lll_transform()
assert abs(T.det())==1
K=T*A*T.T
assert K.det()==64
lower,diag=K.LDLdecomposition(hermitian=False)
assert lower*diag*lower.T==K
x=[0]*18;roots=set();nodes=0
def explore(j,remaining):
 global nodes
 nodes+=1
 if j<0:
  if remaining==0 and any(x):
   v=tuple(x);roots.add(max(v,tuple(-a for a in v)))
  return
 center=-sum(lower[i,j]*x[i] for i in range(j+1,18))
 bound=remaining/diag[j,j]
 if bound<0:return
 radius=isqrt(int(bound.p)//int(bound.q))+2
 lo=int(s.floor(center))-radius
 hi=int(s.ceiling(center))+radius
 for a in range(lo,hi+1):
  t=remaining-diag[j,j]*(s.Rational(a)-center)**2
  if t<0:continue
  x[j]=a
  explore(j-1,t)
explore(17,s.Integer(2))
assert len(roots)==14
V=s.Matrix.hstack(*(s.Matrix(v) for v in sorted(roots)))
assert V.rank()==12
assert all((s.Matrix(v).T*K*s.Matrix(v))[0]==2 for v in roots)
result={"bound":"RQT-126","N18_rank":18,"N18_determinant":64,
 "unimodular_reduction_determinant":int(T.det()),
 "exact_root_pairs":14,"norm_minus_two_roots":28,"root_span_rank":12,
 "exact_enumeration_nodes":nodes,
 "minimum_roots_for_E8_minus_one_squared":480,
 "E8_minus_one_squared_in_this_complement":"IMPOSSIBLE",
 "status":"PASS exhaustive enumeration; STOP proposed E8 summand extraction",
 "next":"Try a different primitive U embedding, or direct isometry on the Fermat line Gram",
 "general_Hodge_conjecture":"OPEN"}
(root/'rqt-126-results.json').write_text(json.dumps(result,indent=2))
(root/'rqt-126-roots.json').write_text(json.dumps([list(v) for v in sorted(roots)],indent=2))
print(json.dumps(result,indent=2))
