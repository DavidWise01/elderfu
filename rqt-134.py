#!/usr/bin/env python3
"""RQT-134: exact 4-tick Fermat K3 cycle orbit closure.
Requires rqt-133.py and its RQT-114/121/132 dependencies in same directory.
"""
from pathlib import Path
from runpy import run_path
import sympy as s,mpmath as mp,json
root=Path(__file__).resolve().parent
p=run_path(str(root/'rqt-133.py'))
X,H,W,n=p['X'],p['H'],p['W'],p['n']
delta=s.eye(22)[:,20]
states=[X**k*delta for k in range(5)]
assert X.T*H*X==H and X**4==s.eye(22) and X.det()==-1
assert states[4]==states[0]
assert all(all(x.is_Integer for x in v) for v in states)
assert all((v.T*H*v)[0]==-2 for v in states)
assert all((states[k].T*H*states[(k+1)%4])[0]==1 for k in range(4))
assert all((states[k].T*H*states[(k+2)%4])[0]==0 for k in range(4))
assert states[2][:20,0]==n
assert states[2][20,0]==-1 and states[2][21,0]==0
assert states[3][:20,0]==W*n
assert states[3][20,0]==0 and states[3][21,0]==-1
assert states[4][:20,0]==s.zeros(20,1)
assert list(states[4][20:,0])==[1,0]
J=X[20:,20:];assert J==s.Matrix([[0,-1],[1,0]]) and J**4==s.eye(2)
mp.mp.dps=65
I=mp.gamma(mp.mpf(1)/4)**3/(64*mp.gamma(mp.mpf(3)/4))
base=-2*mp.sqrt(2)*I
periods=[base*(1j)**k for k in range(5)]
for k,v in enumerate(states):
 a,b=[int(z) for z in v[20:,0]]
 assert abs(base*(a+1j*b)-periods[k])<mp.mpf('1e-50')
assert periods[0]==periods[4]
result={'bound':134,'status':'PASS full four-tick 22D integral and period closure',
'Gram_determinant':str(H.det()),'action_determinant':int(X.det()),
'cycle_states':[[int(z) for z in v] for v in states],
'algebraic_correction_tick_2':[int(z) for z in n],
'algebraic_correction_tick_3':[int(z) for z in W*n],
'periods':[mp.nstr(v,40) for v in periods],
'phase_multipliers':['1','i','-1','-i','1'],
'cycle_squares':[-2]*5,'adjacent_intersections':[1]*4,
'opposite_intersections':[0]*4,
'dependency':'RQT-118 Pham raw pairing; RQT-121 vertex orientations',
'general_Hodge_conjecture':'OPEN'}
(root/'rqt-134-results.json').write_text(json.dumps(result,indent=2))
print(json.dumps({k:v for k,v in result.items() if k not in ('cycle_states','algebraic_correction_tick_3')},indent=2))
