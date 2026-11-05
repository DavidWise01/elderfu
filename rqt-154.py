#!/usr/bin/env python3
"""RQT-154: fixed points destroy norm surjectivity by an exact index of four."""
from pathlib import Path
from runpy import run_path
import sympy as s,json
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
p=Path(__file__).resolve().parent
r=run_path(str(p/'rqt-147.py'))
X,P,K=r['X'],r['P'],r['K']
I=s.eye(22);h=s.Matrix([1,1,1,1]+[0]*18);e0=I[:,0]
N=I+X+X**2+X**3
assert X**4==I and N*e0==h and X*h==h and N*h==4*h
assert abs(P.det())==1 and N*K==s.zeros(22,21)
assert (X-I).rank()==21 and (X*K-K).rank()==21
assert s.Matrix.hstack(h,(X-I).nullspace()[0]).rank()==1
assert N==h*s.Matrix([[1]*20+[0]*2])
# On fixed groups, N: Z*h -> Z*h is multiplication by four.
assert smith_normal_form(s.Matrix([[4]]),domain=ZZ)==s.Matrix([[4]])
A=P.inv()*X*P;Y=A[1:,1:];delta=A[1:,0];D=Y-s.eye(21)
assert A[:1,:]==s.Matrix([[1]+[0]*21])
assert delta==s.Matrix([1,1,1,1]+[0]*17)
assert K*delta==(X-I)*e0
assert s.eye(21)+Y+Y**2+Y**3==s.zeros(21)
v=D.inv()*delta
assert all((4*t).is_Integer for t in v)
assert any(not (2*t).is_Integer for t in v)
assert len({tuple((k*t)%1 for t in v) for k in range(4)})==4
assert (X-I)*(4*e0-h)==4*K*delta
S=smith_normal_form(D,domain=ZZ)
T=smith_normal_form(D.row_join(delta),domain=ZZ)
assert [abs(int(S[j,j])) for j in range(21)]==[1]*14+[4]*7
assert [abs(int(T[j,j])) for j in range(21)]==[1]*15+[4]*6
result={'RQT':154,'status':'PASS','K_fixed':'0',
 'M_fixed':'Z*h','target_fixed':'Z*h',
 'fixed_norm_map':'times four','fixed_cokernel':'Z/4',
 'unrestricted_norm_surjective':True,
 'connecting':'h -> [(X-I)e0]','connecting_kernel':'4Z*h',
 'connecting_image':'Z/4','connecting_order':4,
 'H1_K':'(Z/4)^7','H1_M':'(Z/4)^6',
 'scope':'Conditional Fermat marking (RQT-118/121); general Hodge OPEN'}
(p/'rqt-154-results.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
