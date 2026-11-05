#!/usr/bin/env python3
"""RQT-153 exact degree-zero Tate quotient."""
from pathlib import Path
from runpy import run_path
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
p=Path(__file__).resolve().parent
r=run_path(str(p/'rqt-147.py'))
X,P=r['X'],r['P']
I=s.eye(22);h=s.Matrix([1,1,1,1]+[0]*18)
N=I+X+X**2+X**3
assert X**4==I and X*h==h and N*I[:,0]==h
assert (X-I).rank()==21 and N.rank()==1
assert N==h*s.Matrix([[1]*20+[0]*2])
assert N*P==s.Matrix.hstack(h,s.zeros(22,21))
C=(P.inv()*(X-I))[1:,:]
S=smith_normal_form(C,domain=ZZ)
assert [abs(int(S[j,j])) for j in range(21)]==[1]*15+[4]*6
assert X*(h/4)==h/4 and N*(h/4)==h
print("RQT-153 PASS: Tate H0=0; Tate H-1=(Z/4)^6; equivariant integral section absent")
