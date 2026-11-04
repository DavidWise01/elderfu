#!/usr/bin/env python3
"""RQT-125: integral hyperbolic-plane split of actual Fermat line lattice."""
import runpy,itertools,json
from pathlib import Path
import sympy as s
root=Path(__file__).resolve().parent
r=runpy.run_path(str(root/'rqt-114.py'))
G,B=r['G'],r['B'];piv=list(r['pivots'])
assert G.shape==(48,48) and B.det()==-64
h=s.zeros(48,1)
for j in range(4):h[j]=1
L=s.eye(48)[:,0];f=h-L
assert (h.T*G*h)[0]==4 and (f.T*G*f)[0]==0
section_index=next(j for j in range(48) if (f.T*G*s.eye(48)[:,j])[0]==1)
section=s.eye(48)[:,section_index];e=f+section
assert (section.T*G*section)[0]==-2
C=B.inv()*G.extract(piv,list(range(48)))*s.Matrix.hstack(f,e)
assert all(x.is_Integer for x in C)
assert C.T*B*C==s.Matrix([[0,1],[1,0]])
v,w=C[:,0],C[:,1]
perp=[]
for j in range(20):
 x=s.eye(20)[:,j]
 perp.append(x-(x.T*B*w)[0]*v-(x.T*B*v)[0]*w)
for indices in itertools.combinations(range(20),18):
 P=s.Matrix.hstack(v,w,*[perp[j] for j in indices])
 if abs(P.det())==1:break
else:raise AssertionError("integral basis not found")
N=(P.T*B*P)[2:,2:]
assert P.T*B*P==s.diag(s.Matrix([[0,1],[1,0]]),N)
assert N.det()==64
assert all(x.is_Integer for x in P.inv())
assert all((-N)[:k,:k].det()>0 for k in range(1,19))
result={"section_line_0_based":section_index,"hyperplane_lines":[0,1,2,3],
 "P_determinant":int(P.det()),"N18_determinant":int(N.det()),
 "N18_negative_definite":True,"U_Gram":[[0,1],[1,0]],
 "P_rows":[[int(x) for x in P.row(j)] for j in range(20)],
 "N18_rows":[[int(x) for x in N.row(j)] for j in range(18)],
 "status":"PASS integral U split; STOP explicit rank-18 E8(-1)^2 + <-8>^2 decomposition",
 "Hodge_conjecture":"OPEN"}
(root/'rqt-125-results.json').write_text(json.dumps(result,indent=2))
print(json.dumps({k:v for k,v in result.items() if k not in ('P_rows','N18_rows')},indent=2))
