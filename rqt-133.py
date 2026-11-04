#!/usr/bin/env python3
"""RQT-133 exact Fermat Pham-cycle transport; depends on RQT-121, RQT-132."""
from pathlib import Path
from runpy import run_path
import sympy as s,json
root=Path(__file__).resolve().parent
a=run_path(str(root/'rqt-121.py'))
g=run_path(str(root/'rqt-132.py'))
B,G,piv=a['B'],a['G'],list(a['piv'])
d,r=a['d'],a['r']
D,R=a['D'],a['R']
W,images=g['W'],g['images']
assert len(images)==48
assert all(G[i,j]==G[images[i],images[j]] for i in range(48) for j in range(48))
H=B.row_join(s.Matrix.hstack(d,r)).col_join(s.Matrix.hstack(d,r).T.row_join(s.Matrix([[-2,1],[1,-2]])))
assert H.det()==-1
inv=[images.index(j) for j in range(48)]
pair2=s.Matrix([R[inv[j]] for j in range(48)])
n=B.inv()*(s.Matrix([pair2[j] for j in piv])+d)
assert all(z.is_Integer for z in n)
assert G[:,piv]*(n-B.inv()*d)==pair2
X=s.zeros(22)
X[:20,:20]=W
X[21,20]=1
X[:20,21]=n
X[20,21]=-1
assert all(z.is_Integer for z in X)
assert X.T*H*X==H and X**4==s.eye(22) and X.det()==-1
for k in range(4):
 vec=(X**k)[:,20]
 expected=s.Matrix(D)
 for _ in range(k):expected=s.Matrix([expected[inv[j]] for j in range(48)])
 actual=G[:,piv]*vec[:20,0]+s.Matrix.hstack(s.Matrix(D),s.Matrix(R))*vec[20:,0]
 assert actual==expected
J=s.Matrix([[0,-1],[1,0]])
assert X[20:,20:]==J
result={'RQT':133,'geometric_integral_basis_dim':22,'correction_vector':[int(z) for z in n],
 'all_line_pairing_comparisons':192,'integral':True,'gram_isometry':True,
 'fourth_power_identity':True,'determinant':int(X.det()),
 'transcendental_quotient_action':[[int(z) for z in row] for row in J.tolist()],
 'orientation_dependency':'RQT-118 Pham pairing and RQT-121 local signs',
 'general_Hodge_conjecture':'OPEN'}
(root/'rqt-133-results.json').write_text(json.dumps(result,indent=2))
(root/'rqt-133-X-22x22.txt').write_text(str(X))
print(json.dumps(result,indent=2))
