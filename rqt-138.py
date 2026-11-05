#!/usr/bin/env python3
"""RQT-138 exact action on the 512 glue classes of RQT-137."""
from pathlib import Path
from runpy import run_path
import itertools,collections,json
import sympy as s
root=Path(__file__).resolve().parent
r=run_path(str(root/"rqt-137.py"))
g=run_path(str(root/"rqt-133.py"))
Z=r["Z"];X=g["X"]
generators=r["gens"] if "gens" in r else r["generators"]
E=s.Matrix.hstack(*generators)
assert Z.shape==X.shape==(22,22) and E.shape==(22,8)
assert abs(Z.det())==512 and X**4==s.eye(22)
Zi=Z.inv(); A=Zi*X*Z
assert all(t.is_Integer for t in A)
V=[tuple(int(t)%4 for t in 4*Zi*E[:,j]) for j in range(8)]
classes={}
for a in range(4):
 for bits in itertools.product((0,1),repeat=7):
  label=(a,)+bits
  state=tuple(sum(label[j]*V[j][i] for j in range(8))%4 for i in range(22))
  assert state not in classes
  classes[state]=label
assert len(classes)==512
def action(v):return tuple(int(x)%4 for x in A*s.Matrix(v))
f={v:action(v) for v in classes}
assert set(f.values())==set(classes)
images=[classes[f[v]] for v in V]
expected=[(1,0,0,1,0,0,0,0)]+[tuple(int(i==j) for i in range(8)) for j in range(1,8)]
assert images==expected
for v,label in classes.items():
 a,b1,b2,b3,b4,b5,b6,b7=label
 assert classes[f[v]]==(a,b1,b2,(b3+a)%2,b4,b5,b6,b7)
seen=set();counts=collections.Counter();orbits=[]
for v in classes:
 if v in seen:continue
 cycle=[];w=v
 while w not in seen:
  seen.add(w);cycle.append(classes[w]);w=f[w]
 assert w==v
 counts[len(cycle)]+=1;orbits.append(cycle)
assert len(seen)==512 and counts=={1:256,2:128}
def iterate(v,k):
 for _ in range(k):v=f[v]
 return v
fixed={str(k):sum(iterate(v,k)==v for v in classes) for k in (1,2,3,4)}
assert fixed=={"1":256,"2":512,"3":256,"4":512}
result={"RQT":138,"ambient_action_order":4,"glue_action_order":2,
 "quotient":"Z/4 + (Z/2)^7",
 "generator_images":[list(t) for t in images],
 "rule":"(a;b1,b2,b3,b4,b5,b6,b7)->(a;b1,b2,b3+a mod 2,b4,b5,b6,b7)",
 "orbits_by_length":dict(counts),"fixed_by_power":fixed,"orbit_listing":orbits,
 "checked_classes":512,"status":"PASS",
 "dependency":"RQT-118/121 Pham orientations and RQT-136/137 bases",
 "general_Hodge":"OPEN"}
(root/"rqt-138-results.json").write_text(json.dumps(result,indent=2))
print("PASS",counts,fixed)
