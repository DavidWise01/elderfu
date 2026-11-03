#!/usr/bin/env python3
"""RQT-115 exact period check, building on reproducible RQT-114 gluing."""
from pathlib import Path
from runpy import run_path
import sympy as s
ns=run_path(str(Path(__file__).with_name("rqt-114.py")))
H=ns["H"];u=ns["u"];v=ns["v"]
assert H.shape==(22,22)
t1=s.Matrix.vstack(-8*s.Matrix(u),s.Matrix([8,0]))
t2=s.Matrix.vstack(-8*s.Matrix(v),s.Matrix([0,8]))
omega=t1+s.I*t2
pair=lambda x,y:s.expand((x.T*H*y)[0])
assert pair(t1,t1)==8 and pair(t2,t2)==8 and pair(t1,t2)==0
assert s.simplify(pair(omega,omega))==0
assert s.simplify(pair(omega,s.conjugate(omega)))==16
assert all(s.simplify(pair(s.eye(22)[:,j],omega))==0 for j in range(20))
assert s.simplify(pair(s.eye(22)[:,20],omega))==1
assert s.simplify(pair(s.eye(22)[:,21],omega))==s.I
assert s.simplify((-t2+s.I*t1)-s.I*omega)==s.zeros(22,1)
assert H.det()==-1
assert all(x.is_Integer for x in H)
assert all((H[j,j]/2).is_Integer for j in range(22))
print("PASS: omega²=0, omega·conjugate(omega)=16")
print("PASS: omega orthogonal to 20 chosen algebraic line generators")
print("PASS: T-quarter-turn preserves period line with multiplier i")
print("STOP: a geometric marking/actual Fermat periods have not been computed")
