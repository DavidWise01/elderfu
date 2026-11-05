#!/usr/bin/env python3
"""RQT-152: exact minimal denominator of the rational equivariant section."""
from pathlib import Path
from runpy import run_path
import sympy as s,json
p=Path(__file__).resolve().parent
a=run_path(str(p/'rqt-133.py'))
b=run_path(str(p/'rqt-147.py'))
X=a['X'];P=b['P'];K=b['K']
I=s.eye(22);e=I[:,0];h=s.Matrix([1,1,1,1]+[0]*18)
N=I+X+X**2+X**3
assert X**4==I and N.rank()==1 and (X-I).rank()==21
assert N*e==h and X*h==h and N*h==4*h
assert abs(P.det())==1 and N*K==s.zeros(22,21)
assert s.igcd(*(int(t) for t in h))==1
assert len((X-I).nullspace())==1
assert s.Matrix.hstack(h,(X-I).nullspace()[0]).rank()==1
q=h/4
assert X*q==q and N*q==h
assert all((4*t).is_Integer for t in q)
assert all(not all((d*t).is_Integer for t in q) for d in (1,2,3))
# Any rational X-fixed preimage of h is r*h; norm 4*r*h=h implies r=1/4.
transforms=[('identity',I),('splitting',P)]
for j in range(21):
 B=I.copy();B[j,j]=-1;transforms.append((f'sign{j}',B))
 B=I.copy();B[j,j]=0;B[j+1,j+1]=0
 B[j,j+1]=B[j+1,j]=1;transforms.append((f'swap{j}',B))
 B=I.copy();B[j,j+1]=j+1;transforms.append((f'shear{j}',B))
assert len(transforms)==65
for name,B in transforms:
 assert abs(B.det())==1
 qb=B.inv()*q
 assert all((4*t).is_Integer for t in qb)
 assert all(not all((d*t).is_Integer for t in qb) for d in (1,2,3))
 assert (B.inv()*X*B)*qb==qb
 assert (B.inv()*N*B)*qb==B.inv()*h
# Invariance for all B in GL(22,Z) follows from B Z^22=Z^22.
shifts=[s.zeros(21,1)]
for j in range(21):
 v=s.eye(21)[:,j];shifts.extend((v,-v,2*v,-2*v))
for t in range(256):
 shifts.append(s.Matrix([((t*(j+3)+j*j+2*j)//(j+2))%7-3 for j in range(21)]))
assert len(shifts)==341 and len({tuple(v) for v in shifts})==341
for a in shifts:
 section=e+K*a;correction=q-section
 assert N*section==h and X*section!=section
 assert N*correction==s.zeros(22,1)
 assert (P.inv()*correction)[0]==0
 assert (X-I)*(section+correction)==s.zeros(22,1)
 assert any(not t.is_Integer for t in correction)
result={'RQT':152,'status':'PASS',
 'rational_equivariant_section':'h/4','unique':True,
 'fixed_rational_rank':1,'minimal_denominator':4,
 'unimodular_basis_tests':65,'integral_section_shifts':341,
 'basis_invariance':'all GL(22,Z), by lattice equivalence',
 'obstruction_order':4,
 'scope':'Fermat quartic marking conditional on RQT-118/121',
 'Hodge_conjecture':'OPEN'}
(p/'rqt-152-results.json').write_text(json.dumps(result,indent=2))
(p/'rqt-152-section-22-vector.txt').write_text(str(q))
print(json.dumps(result,indent=2))
