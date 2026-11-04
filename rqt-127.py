#!/usr/bin/env python3
"""RQT-127: exact finite search over 20 alternative primitive U embeddings.
Requires rqt-114.py. Floating point is used only to find a unimodular LLL
basis; root enumeration is exhaustive with exact rational LDL arithmetic.
"""
import runpy,itertools,json
from pathlib import Path
from math import isqrt
import numpy as np
import sympy as s
root=Path(__file__).resolve().parent
base=runpy.run_path(str(root/'rqt-114.py'))
G,B,piv=base['G'],base['B'],list(base['pivots'])
E=s.eye(48);C=B.inv()*G.extract(piv,list(range(48)))
h=sum((E[:,j] for j in range(4)),s.zeros(48,1))
CASES=[
((0,1,6),7),((0,1,7),6),((0,1,10),4),((0,1,11),4),
((0,1,14),4),((0,1,15),4),((0,1,18),4),((0,1,19),5),
((29,44,45,46,47),0),((19,23,24,27,31),0),
((0,4,8,12,19),0),((34,38,39,42,46),0),
((34,38,42,43,46),0),((16,17,18,19,47),0),
((0,1,2,3,33),0),((32,35,36,40,44),1),
((34,44,45,46,47),0),((35,39,43,46,47),1),
((28,29,30,31,45),0),((6,16,17,18,19),0)]
def complement(f,section):
 X=C*s.Matrix.hstack(f,f+section)
 assert all(z.is_Integer for z in X)
 v,w=X[:,0],X[:,1]
 assert X.T*B*X==s.Matrix([[0,1],[1,0]])
 projections=[]
 for j in range(20):
  e=s.eye(20)[:,j]
  projections.append(e-(e.T*B*w)[0]*v-(e.T*B*v)[0]*w)
 for subset in itertools.combinations(range(20),18):
  P=s.Matrix.hstack(v,w,*[projections[j] for j in subset])
  if abs(P.det(method='domain-ge'))==1:
   N=-(P.T*B*P)[2:,2:]
   assert N.det()==64
   return N
 raise AssertionError('integral complement not found')
def exact_root_count(A):
 L=np.linalg.cholesky(np.asarray(A.tolist(),dtype=float)).T
 embedding=s.Matrix(np.rint(L*10000).astype('int64').tolist()).T
 _,T=embedding.lll_transform()
 assert abs(T.det())==1
 K=T*A*T.T
 low,diag=K.LDLdecomposition(hermitian=False)
 assert low*diag*low.T==K
 x=[0]*18;roots=set();nodes=[0]
 def dfs(j,remaining):
  nodes[0]+=1
  if j<0:
   if remaining==0 and any(x):
    v=tuple(x);roots.add(max(v,tuple(-z for z in v)))
   return
  center=-sum(low[i,j]*x[i] for i in range(j+1,18))
  rad=isqrt(int((remaining/diag[j,j]).p)//int((remaining/diag[j,j]).q))+2
  for a in range(int(s.floor(center))-rad,int(s.ceiling(center))+rad+1):
   rr=remaining-diag[j,j]*(s.Rational(a)-center)**2
   if rr>=0:x[j]=a;dfs(j-1,rr)
 dfs(17,s.Integer(2))
 assert all((s.Matrix(v).T*K*s.Matrix(v))[0]==2 for v in roots)
 return 2*len(roots),nodes[0]
results=[]
for ids,j in CASES:
 f=2*h-sum((E[:,k] for k in ids),s.zeros(48,1))
 assert (f.T*G*f)[0]==0 and (f.T*G*E[:,j])[0]==1
 A=complement(f,E[:,j])
 n,nodes=exact_root_count(A)
 assert n==28
 results.append({'subtracted_lines':list(ids),'section':j,'roots':n,
 'nodes':nodes,'degree':int((f.T*G*h)[0])})
output={'bound':'RQT-127','candidates':20,'three_line':8,'five_line':12,
'root_counts':[v['roots'] for v in results],'entries':results,
'E8x2':0,'stop':'Finite samples do not exclude other U embeddings',
'Hodge_conjecture':'OPEN'}
(root/'rqt-127-results.json').write_text(json.dumps(output,indent=2))
print(json.dumps({'candidates':20,'root_counts_unique':[28],
'status':'PASS finite exact enumeration; STOP universal conclusion'},indent=2))
