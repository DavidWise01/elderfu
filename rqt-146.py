#!/usr/bin/env python3
"""RQT-146: arbitrary integral vector wraparound defect; exact arithmetic."""
from pathlib import Path
import sympy as s,json
p=Path(__file__).resolve().parent
X=s.sympify((p/'rqt-133-X-22x22.txt').read_text(),locals={'Matrix':s.Matrix})
I=s.eye(22); N=I+X+X**2+X**3
assert X**4==I and N.rank()==1
h=s.Matrix([1,1,1,1]+[0]*18)
assert N[:,0]==h and X*h==h and N*h==4*h
assert all(N[:,j]==int(N[0,j])*h for j in range(22))
def S(k):return sum((X**j for j in range(k)),s.zeros(22))
pairs=wraps=triples=nonzero=0
for a in range(4):
 for b in range(4):
  carry=(a+b)//4
  D=S(a)+X**a*S(b)-S((a+b)%4)
  assert D==carry*N
  for j in range(22):
   u=I[:,j]
   assert D*u==carry*N*u
   assert (X**((a+b)%4)-I)*u==(X-I)*(S(a)+X**a*S(b))*u
   pairs+=1
   if carry:
    wraps+=1
    nonzero+=int(N*u!=s.zeros(22,1))
  for c in range(4):
   D3=S(a)+X**a*S(b)+X**(a+b)*S(c)-S((a+b+c)%4)
   assert D3==((a+b+c)//4)*N
   triples+=22
assert (pairs,wraps,nonzero,triples)==(352,132,120,1408)
assert [j for j in range(22) if N[:,j]==s.zeros(22,1)]==[20,21]
result={'RQT':146,'pair_tests':pairs,'wrapped_tests':wraps,
 'nonzero_wrapped_defects':nonzero,'triple_tests':triples,
 'norm_rank':1,'norm_image':'Z*h','h_coordinates':[int(v) for v in h],
 'zero_norm_basis_indices':[20,21],
 'identity':'S_a+X^a S_b-S_((a+b)%4)=floor((a+b)/4)*N',
 'scope':'All integer vectors by Z-linearity; special Fermat K3; Hodge conjecture OPEN'}
(p/'rqt-146-results.json').write_text(json.dumps(result,indent=2))
print(json.dumps(result,indent=2))
