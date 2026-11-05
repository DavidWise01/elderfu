#!/usr/bin/env python3
"""RQT-149: integer section-defect 1-cocycle and order-four obstruction."""
from pathlib import Path
from runpy import run_path
import sympy as s,json
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
p=Path(__file__).resolve().parent
v=run_path(str(p/'rqt-147.py'))
X,K,P=v['X'],v['K'],v['P']
I=s.eye(22);e0=I[:,0];h=s.Matrix([1,1,1,1]+[0]*18)
N=I+X+X**2+X**3
assert X**4==I and N*e0==h and N*K==s.zeros(22,21)
assert P==s.Matrix.hstack(e0,K) and abs(P.det())==1
Y=(P.inv()*X*P)[1:,1:];D=Y-s.eye(21)
def defect(k):return (X**(k%4)-I)*e0
coords=[]
for k in range(5):
 z=P.inv()*defect(k)
 assert z[0,0]==0 and K*z[1:,0]==defect(k)
 assert all(x.is_Integer for x in z)
 assert N*defect(k)==s.zeros(22,1)
 coords.append(z[1:,0])
assert coords[0]==coords[4]==s.zeros(21,1)
delta=coords[1]
assert delta==s.Matrix([1,1,1,1]+[0]*17)
assert defect(1)==I[:,4]-I[:,0]
assert sum((Y**k*delta for k in range(4)),s.zeros(21,1))==s.zeros(21,1)
pairs=triples=0
for a in range(4):
 for b in range(4):
  assert coords[(a+b)%4]==coords[a]+Y**a*coords[b]
  assert defect(a+b)==defect(a)+X**a*defect(b)
  pairs+=1
  for c in range(4):
   assert coords[(a+b+c)%4]==coords[a]+Y**a*coords[b]+Y**(a+b)*coords[c]
   triples+=1
assert (pairs,triples)==(16,64)
w=D.inv()*delta
assert next(n for n in (1,2,3,4) if all((n*t).is_Integer for t in w))==4
assert (X-I)*(4*e0-h)==4*defect(1)
assert N*(4*e0-h)==s.zeros(22,1)
S=smith_normal_form(D,domain=ZZ)
assert [abs(int(S[j,j])) for j in range(21)]==[1]*14+[4]*7
out={'RQT':149,'type':'group 1-cocycle (crossed homomorphism)',
 'pair_checks':pairs,'triple_checks':triples,'full_cycle_defect':0,
 'section_defects_22d':[[int(t) for t in defect(k)] for k in range(5)],
 'kernel_coordinates_21d':[[int(t) for t in z] for z in coords],
 'obstruction_order':4,'ambient_coboundary':True,
 'kernel_coboundary':False,'equivariant_section':False,
 'geometric_dependencies':'RQT-118/121 Pham conventions',
 'general_Hodge_conjecture':'OPEN'}
(p/'rqt-149-results.json').write_text(json.dumps(out,indent=2))
(p/'rqt-149-defect-matrix.txt').write_text(str(s.Matrix.hstack(*[defect(k) for k in range(5)])))
print('PASS: 16 pairs, 64 triples, norm-zero closure, obstruction order 4')
