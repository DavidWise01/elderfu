#!/usr/bin/env python3
"""RQT-151: exact block form and integral extension-class gauge invariance."""
from pathlib import Path
from runpy import run_path
import json
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
p=Path(__file__).resolve().parent
R=run_path(str(p/'rqt-147.py'))
X,P,K=R['X'],R['P'],R['K']
I=s.eye(22);e0=I[:,0];h=s.Matrix([1,1,1,1]+[0]*18)
N=I+X+X**2+X**3
assert P==s.Matrix.hstack(e0,K) and P.det()==1
assert N*e0==h and N*K==s.zeros(22,21)
A=P.inv()*X*P;Y=A[1:,1:];c=A[1:,0];D=Y-s.eye(21)
assert A[:1,:]==s.Matrix([[1]+[0]*21])
assert c==s.Matrix([1,1,1,1]+[0]*17)
assert A**4==s.eye(22) and Y**4==s.eye(21)
assert sum((Y**j*c for j in range(4)),s.zeros(21,1))==s.zeros(21,1)
S=smith_normal_form(D,domain=ZZ)
assert [abs(int(S[j,j])) for j in range(21)]==[1]*14+[4]*7
assert next(k for k in range(1,5) if all((k*t).is_Integer for t in D.inv()*c))==4
def shear(a):
 B=s.eye(22);B[1:,0]=a
 return B
shifts=[s.zeros(21,1)]
for j in range(21):
 v=s.eye(21)[:,j];shifts.extend([v,-v,2*v,-2*v])
for t in range(256):
 shifts.append(s.Matrix([((t*(j+3)+j*j+2*j)//(j+2))%7-3 for j in range(21)]))
assert len(shifts)==341 and len(set(tuple(v) for v in shifts))==341
for a in shifts:
 B=shear(a);assert B.det()==1
 Anew=B.inv()*A*B
 assert Anew[:1,:]==s.Matrix([[1]+[0]*21])
 assert Anew[1:,1:]==Y and Anew[1:,0]==c+D*a
 assert Anew**4==s.eye(22)
 assert K*(c+D*a)==(X-I)*(e0+K*a)
 assert all((4*t).is_Integer for t in D.inv()*(c+D*a))
 assert not all((2*t).is_Integer for t in D.inv()*(c+D*a))
for a in range(4):
 for b in range(4):
  ca=sum((Y**j*c for j in range(a)),s.zeros(21,1))
  cb=sum((Y**j*c for j in range(b)),s.zeros(21,1))
  cab=sum((Y**j*c for j in range((a+b)%4)),s.zeros(21,1))
  assert ca+Y**a*cb==cab
assert X*(h/4)==h/4 and N*(h/4)==h
assert not all(t.is_Integer for t in h/4)
result={'RQT':151,'status':'PASS',
 'block_form':'[[1,0],[c,Y]]','c':[int(t) for t in c],
 'restricted_action_smith':[1]*14+[4]*7,
 'section_shift':'c_a=c+(Y-I)a','obstruction_order':4,
 'integral_section_changes':341,'cyclic_pairs':16,
 'integral_equivariant_split':False,
 'rational_equivariant_section':'h/4',
 'scope':'special Fermat marking (RQT-118/121); Hodge conjecture OPEN'}
(p/'rqt-151-results.json').write_text(json.dumps(result,indent=2))
(p/'rqt-151-block-matrix.txt').write_text(str(A))
print(json.dumps({k:v for k,v in result.items() if k!='restricted_action_smith'},indent=2))
