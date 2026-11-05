"""RQT-140: exact finite fixed-lift cohomology check."""
from pathlib import Path
from runpy import run_path
from itertools import product
import sympy as s
import json
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
p=Path(__file__).resolve().parent
Z=run_path(str(p/"rqt-136.py"))["Z"]
X=run_path(str(p/"rqt-133.py"))["X"]
e=s.eye(22);I=s.eye(22)
E=s.Matrix.hstack(2*e[:,0],*[e[:,j]-e[:,0] for j in (1,2,4,10,11,16)],e[:,20])
A=Z.inv()*X*Z
N=I+A+A**2+A**3
assert N==s.diag(4,*([0]*21))
K=(A-I)[1:,1:]
D=smith_normal_form(K,domain=ZZ)
fac=[abs(int(D[j,j])) for j in range(21)]
assert fac==[1]*7+[2]*14
Q=K.inv()*(Z.inv()*(X-I)*E)[1:,:]
assert all((2*x).is_Integer for x in Q)
mod=lambda v:tuple(s.Rational(x)%1 for x in v)
glue=set();obs=set()
for bits in product((0,1),repeat=8):
 b=s.Matrix(bits)
 glue.add(mod(Z.inv()*E*b))
 obs.add(mod(Q*b))
assert len(glue)==len(obs)==256
assert sum(any(v) for v in obs)==255
out={"RQT":140,"Smith":fac,"H1":"(Z/2)^14",
 "fixed_glue":"(Z/2)^8","image":"(Z/2)^8",
 "cokernel":"(Z/2)^6","zero":1,"nonzero":255,
 "scope":"conditional geometric Fermat quartic; general Hodge OPEN"}
(p/"rqt-140-results.json").write_text(json.dumps(out,indent=2))
print(out)
