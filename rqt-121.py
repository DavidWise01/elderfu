#!/usr/bin/env python3
"""RQT-121: exact signed intersection counts at Fermat quartic Pham vertices."""
from itertools import product
from pathlib import Path
import json
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

h=s.sqrt(2)/2
z=h*(1+s.I)
powers=[s.simplify(s.expand_complex(z**k)) for k in range(8)]
def parts(t):return s.simplify(s.re(t)),s.simplify(s.im(t))
def sign(t):
 t=s.simplify(s.expand(t))
 if t==0:return 0
 v=s.sign(t)
 assert v in (-1,1),(t,v)
 return int(v)
matchings=[((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2))]
lines=[]
for fam,pairs in enumerate(matchings):
 for u,v in product((1,3,5,7),repeat=2):
  wpair=next(pair for pair in pairs if 3 in pair)
  j=next(k for k in wpair if k!=3)
  ew=u if wpair==pairs[0] else v
  other=next(pair for pair in pairs if 3 not in pair)
  e=u if other==pairs[0] else v
  lines.append((fam,u,v,j,ew,other,e))
assert len(lines)==48

def intersection(line,offset,eps):
 fam,u,v,j,ew,(a,b),e=line
 lam=-powers[e]
 lr,li=parts(lam)
 total=0
 for mask in product((0,1),repeat=3):
  k=[mask[t]+offset[t] for t in range(3)]
  if (1+2*k[j]-ew-4)%8:continue
  alpha=powers[(1+2*k[a])%8]
  beta=powers[(1+2*k[b])%8]
  ar,ai=parts(alpha);br,bi=parts(beta)
  wr,wi=parts(-lam*beta);er,ei=parts(eps)
  det=s.simplify(ar*wi-ai*wr)
  assert sign(det)!=0
  x=s.simplify((er*wi-ei*wr)/det)
  y=s.simplify((ar*ei-ai*er)/det)
  if sign(x)>0 and sign(y)>0:
   orientation=s.simplify(-ai*bi*li+ai*br*lr-ar*bi*lr-ar*br*li)
   total+=(-1)**(sum(mask)+j)*sign(orientation)
 return total

epsilons=[s.Rational(13,100)+s.I*s.Rational(21,100),
          -s.Rational(17,100)+s.I*s.Rational(23,100)]
vectors=[]
for epsilon in epsilons:
 vectors.append((
 [intersection(line,(0,0,0),epsilon) for line in lines],
 [intersection(line,(1,0,0),epsilon) for line in lines]
 ))
assert vectors[0]==vectors[1]
D,R=vectors[0]
for data in (D,R):
 assert (data.count(0),data.count(1),data.count(-1))==(36,6,6)

P=17
def rankmod(A):
 A=[[int(v)%P for v in row] for row in A];r=0
 for col in range(4):
  p=next((k for k in range(r,len(A)) if A[k][col]),None)
  if p is None:continue
  A[p],A[r]=A[r],A[p]
  q=pow(A[r][col],-1,P);A[r]=[q*v%P for v in A[r]]
  for k in range(len(A)):
   if k!=r:
    factor=A[k][col]
    A[k]=[(x-factor*y)%P for x,y in zip(A[k],A[r])]
  r+=1
  if r==len(A):break
 return r
rows=[]
for fam,u,v,*_ in lines:
 rr=[]
 for (a,b),e in zip(matchings[fam],(u,v)):
  row=[0]*4;row[a]=1;row[b]=pow(2,e,P)
  rr.append(row)
 rows.append(rr)
G=s.zeros(48)
for i in range(48):
 G[i,i]=-2
 for j in range(i+1,48):
  G[i,j]=G[j,i]=int(rankmod(rows[i]+rows[j])<4)
assert G.rank()==20
piv=G.rref()[1];B=G.extract(piv,piv);Bi=B.inv()
assert B.det()==-64
assert [abs(int(smith_normal_form(B,domain=ZZ)[i,i])) for i in range(20)]==[1]*18+[8,8]
d=s.Matrix([D[i] for i in piv]);r=s.Matrix([R[i] for i in piv])
assert all((G[:,piv]*Bi*d)[j]==D[j] for j in range(48))
assert all((G[:,piv]*Bi*r)[j]==R[j] for j in range(48))
shadow=s.Matrix([[(d.T*Bi*d)[0],(d.T*Bi*r)[0]],
                 [(r.T*Bi*d)[0],(r.T*Bi*r)[0]]])
pham=s.Matrix([[-2,1],[1,-2]])
trans=pham-shadow
assert shadow==s.Matrix([[-s.Rational(17,8),1],[1,-s.Rational(17,8)]])
assert trans==s.diag(s.Rational(1,8),s.Rational(1,8))
assert 64*trans==s.diag(8,8)
result={'RQT':121,'perturbations_agree':True,'line_count':48,
 'Delta_line_intersections':D,'rotated_line_intersections':R,
 'each_cycle_counts_zero_positive_negative':[36,6,6],
 'algebraic_shadow_gram':[[str(shadow[i,j]) for j in range(2)] for i in range(2)],
 'transcendental_gram':[[str(trans[i,j]) for j in range(2)] for i in range(2)],
 'eightfold_scaled_gram':[[int(64*trans[i,j]) for j in range(2)] for i in range(2)],
 'caveat':'Depends on standard Pham cycle pairing/orientation; no full H2 marking',
 'Hodge_conjecture':'OPEN'}
Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
