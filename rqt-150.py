#!/usr/bin/env python3
"""RQT-150: all integral section changes preserve the connecting H1 class."""
from pathlib import Path
from runpy import run_path
import json
import sympy as s
p=Path(__file__).resolve().parent
r=run_path(str(p/'rqt-147.py'))
X,P,K=r['X'],r['P'],r['K']
I=s.eye(22);N=I+X+X**2+X**3
e=I[:,0];h=s.Matrix([1,1,1,1]+[0]*18)
assert P==s.Matrix.hstack(e,K) and abs(P.det())==1
assert N*e==h and N*K==s.zeros(22,21)
Y=(P.inv()*X*P)[1:,1:];D=Y-s.eye(21)
assert P.inv()*X*K==s.Matrix.vstack(s.zeros(1,21),Y)
delta=(P.inv()*(X-I)*e)[1:,0]
assert delta==s.Matrix([1,1,1,1]+[0]*17)
assert D.det()!=0
assert all((4*x).is_Integer for x in D.inv()*delta)
assert not all((2*x).is_Integer for x in D.inv()*delta)
shifts=[s.zeros(21,1)]
for j in range(21):
 a=s.eye(21)[:,j]
 shifts.extend([a,-a,2*a,-2*a])
for t in range(256):
 shifts.append(s.Matrix([((t*(j+3)+j*j+2*j)//(j+2))%7-3 for j in range(21)]))
assert len(shifts)==341
mod=lambda a:tuple(s.Rational(x)%1 for x in a)
tick_checks=0
for a in shifts:
 k=K*a; sec=e+k
 assert N*sec==h
 change=(X-I)*sec
 assert change==(X-I)*e+K*D*a
 coords=(P.inv()*change)[1:,0]
 assert coords==delta+D*a
 assert mod(D.inv()*coords)==mod(D.inv()*delta)
 assert N*change==s.zeros(22,1)
 assert (X-I)*(4*sec-h)==4*change
 assert N*(4*sec-h)==s.zeros(22,1)
 assert not all((2*x).is_Integer for x in D.inv()*coords)
 for tick in range(5):
  drift=(X**tick-I)*sec
  assert drift==(X-I)*sum((X**q*sec for q in range(tick)),s.zeros(22,1))
  assert drift==(X**tick-I)*e+(X**tick-I)*k
  assert N*drift==s.zeros(22,1)
  if tick==4:assert drift==s.zeros(22,1)
  tick_checks+=1
assert tick_checks==1705
output={'RQT':150,'status':'PASS','tested_integral_sections':341,
'tick_checks':1705,'all_integer_shifts_proved_by_formula':True,
'formula':'delta(e0+K*a)=delta(e0)+K*(Y-I)*a',
'obstruction_order':4,'equivariant_integral_section':False,
'Pham_orientation_dependencies':'RQT-118 and RQT-121',
'general_Hodge_conjecture':'OPEN'}
(p/'rqt-150-results.json').write_text(json.dumps(output,indent=2))
print(json.dumps(output,indent=2))
