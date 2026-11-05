#!/usr/bin/env python3
"""RQT-148: exact connecting morphism for Fermat K3 norm sequence.
Run with rqt-147.py and rqt-133.py in the same directory.
"""
from pathlib import Path
from runpy import run_path
import sympy as s,json
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
p=Path(__file__).resolve().parent
v=run_path(str(p/'rqt-147.py'))
X,K,P=v['X'],v['K'],v['P']
I=s.eye(22);N=I+X+X**2+X**3
h=s.Matrix([1,1,1,1]+[0]*18)
e0=I[:,0]
assert P==s.Matrix.hstack(e0,K) and P.det(method='domain-ge')==1
assert N*e0==h and N*K==s.zeros(22,21)
assert X*h==h and N*h==4*h
assert (X-I).rank()==21 and N.rank()==1
A=P.inv()*X*P
assert A[0,0]==1 and A[:1,1:]==s.zeros(1,21)
Y=A[1:,1:]; delta=A[1:,0];D=Y-s.eye(21)
assert Y**4==s.eye(21) and D.det()!=0
assert K*delta==(X-I)*e0
assert s.eye(21)+Y+Y**2+Y**3==s.zeros(21)
def smith_diagonal(M):
 S=smith_normal_form(M,domain=ZZ)
 return [abs(int(S[i,i])) for i in range(min(S.rows,S.cols))]
assert smith_diagonal(D)==[1]*14+[4]*7
assert smith_diagonal(D.row_join(delta))==[1]*15+[4]*6
w=D.inv()*delta
assert all((4*z).is_Integer for z in w)
assert not all((2*z).is_Integer for z in w)
assert K*(4*delta)==(X-I)*(4*e0-h)
assert N*(4*e0-h)==s.zeros(22,1)
out={'RQT':148,'long_exact_segment':
 '0 -> Z --4--> Z --connecting--> (Z/4)^7 -> (Z/4)^6 -> 0',
 'H1_kernel':'(Z/4)^7','H1_ambient':'(Z/4)^6',
 'Smith_difference':[1]*14+[4]*7,
 'Smith_augment':[1]*15+[4]*6,
 'connecting_vector':[int(z) for z in delta],
 'connecting_order':4,
 'connecting_fractional_coordinates':[str(z%1) for z in w],
 'image_connecting':'Z/4','kernel_connecting':'4Z*h',
 'caveat':'Special Fermat K3 marking; RQT-118/121 orientations',
 'general_Hodge_conjecture':'OPEN'}
(p/'rqt-148-results.json').write_text(json.dumps(out,indent=2))
(p/'rqt-148-difference-21x21.txt').write_text(str(D))
print(json.dumps(out,indent=2))
