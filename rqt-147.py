#!/usr/bin/env python3
"""RQT-147: exact integral norm sequence, splitting, equivariant obstruction.
Requires rqt-133.py and rqt-122.py on the same repository branch.
"""
from pathlib import Path
from runpy import run_path
import sympy as s,json
root=Path(__file__).resolve().parent
X=run_path(str(root/'rqt-133.py'))['X']
H=run_path(str(root/'rqt-122.py'))['H']
I=s.eye(22);N=I+X+X**2+X**3
h=s.Matrix([1,1,1,1]+[0]*18);e=I[:,0]
assert X**4==I and X.T*H*X==H and H.det()==-1
assert (h.T*H*h)[0]==4 and X*h==h and N*e==h and N*h==4*h
assert N.rank()==1 and (X-I).rank()==21
assert all(N[:,j]==N[0,j]*h for j in range(22))
row=next(N.row(i) for i in range(22) if any(N.row(i)))
g=s.igcd(*[int(x) for x in row])
T=s.Matrix([list(row/g)]);V=I.copy()
for j in range(1,22):
 a,b=T[0,0],T[0,j]
 if b==0:continue
 u,v,d=s.gcdex(a,b)
 c0,cj=T[:,0],T[:,j]
 T[:,0]=u*c0+v*cj
 T[:,j]=(-b/d)*c0+(a/d)*cj
 c0,cj=V[:,0],V[:,j]
 V[:,0]=u*c0+v*cj
 V[:,j]=(-b/d)*c0+(a/d)*cj
K=V[:,1:];P=s.Matrix.hstack(e,K)
assert N*K==s.zeros(22,21) and K.rank()==21
assert abs(V.det(method='domain-ge'))==1
assert P.det(method='domain-ge')==1
assert P.inv()*K==s.Matrix.vstack(s.zeros(1,21),s.eye(21))
delta=(X-I)*e
assert delta==I[:,4]-I[:,0] and N*delta==s.zeros(22,1)
assert N*(4*e-h)==s.zeros(22,1)
assert (X-I)*(4*e-h)==4*delta
assert len((X-I).nullspace())==1
assert s.Matrix.hstack(h,(X-I).nullspace()[0]).rank()==1
# If n*delta=(X-I)k for k in ker(N), then n*e-k=m*h
# and applying N forces n*h=4*m*h, hence 4 divides n.
out={'RQT':147,'kernel_rank':21,'section':'s(h)=e0',
'unimodular_basis_det':1,'norm_image':'Z*h',
'fixed_integral_lattice':'Z*h','h_square':4,
'delta_22d':[int(x) for x in delta],
'equivariant_section':False,'obstruction_order':4,
'fourfold_witness':'4e0-h',
'boundary':'Integral split PASS; X-equivariant split IMPOSSIBLE',
'dependency':'RQT-118/121 Pham geometric intersection conventions',
'general_Hodge_conjecture':'OPEN'}
(root/'rqt-147-results.json').write_text(json.dumps(out,indent=2))
(root/'rqt-147-kernel-basis.txt').write_text(str(K))
(root/'rqt-147-splitting-basis.txt').write_text(str(P))
print(json.dumps(out,indent=2))
