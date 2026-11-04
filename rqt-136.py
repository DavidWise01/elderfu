#!/usr/bin/env python3
"""RQT-136: primitive integer kernels, exact Gram matrices and gluing index."""
from pathlib import Path
from runpy import run_path
import sympy as s,json
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
root=Path(__file__).resolve().parent
old=run_path(str(root/"rqt-133.py"))
X,H=old["X"],old["H"]
I=s.eye(22)
assert X**4==I and H.det()==-1

def primitive_kernel(A):
    T=s.Matrix(A);V=s.eye(T.cols);rank=0
    for row in range(T.rows):
        j=next((j for j in range(rank,T.cols) if T[row,j]),None)
        if j is None:continue
        if j!=rank:T.col_swap(j,rank);V.col_swap(j,rank)
        for j in range(rank+1,T.cols):
            a,b=T[row,rank],T[row,j]
            if not b:continue
            u,v,g=s.gcdex(a,b)
            assert u*a+v*b==g
            c,d=T[:,rank],T[:,j]
            T[:,rank]=u*c+v*d
            T[:,j]=(-b/g)*c+(a/g)*d
            c,d=V[:,rank],V[:,j]
            V[:,rank]=u*c+v*d
            V[:,j]=(-b/g)*c+(a/g)*d
        if T[row,rank]<0:
            T[:,rank]=-T[:,rank];V[:,rank]=-V[:,rank]
        rank+=1
        if rank==T.cols:break
    K=V[:,rank:]
    assert abs(V.det(method="domain-ge"))==1
    assert A*K==s.zeros(A.rows,K.cols)
    assert K.cols==A.cols-A.rank()
    return K

operators={"fixed_plus":X-I,"reversed_minus":X+I,"quarter_turn":X**2+I}
bases={name:primitive_kernel(A) for name,A in operators.items()}
ranks={name:K.cols for name,K in bases.items()}
assert ranks=={"fixed_plus":1,"reversed_minus":7,"quarter_turn":14}
grams={name:K.T*H*K for name,K in bases.items()}
determinants={name:int(Q.det()) for name,Q in grams.items()}
assert determinants=={"fixed_plus":4,"reversed_minus":-256,"quarter_turn":256}
for name,K in bases.items():
    (root/(name+"-basis.txt")).write_text(str(K))
    (root/(name+"-gram.txt")).write_text(str(grams[name]))
Z=s.Matrix.hstack(*(bases[name] for name in operators))
assert Z.shape==(22,22)
assert Z.T*H*Z==s.diag(*(grams[name] for name in operators))
index=abs(int(Z.det(method="domain-ge")))
assert index==512
S=smith_normal_form(Z,domain=ZZ)
factors=[abs(int(S[j,j])) for j in range(22)]
assert factors==[1]*14+[2]*7+[4]
assert index**2==abs(int((Z.T*H*Z).det()))
result={"RQT":136,"ranks":ranks,"Gram_determinants":determinants,
"combined_index":index,"Smith_invariants":factors,
"quotient":"(Z/2)^7 + Z/4",
"integral_orthogonal_direct_sum":False,
"next":"Construct explicit glue cosets",
"Pham_orientation_dependency":"RQT-118 and RQT-121",
"general_Hodge":"OPEN"}
(root/"rqt-136-results.json").write_text(json.dumps(result,indent=2))
(root/"combined-basis.txt").write_text(str(Z))
print(json.dumps(result,indent=2))
