from fractions import Fraction as F
# Degree k pullback action of multiplication-by-m on elliptic E is m**k.
maps=[0,1,2]
coeffs=[[F(1),F(0),F(0)],[F(-3,2),F(2),F(-1,2)],[F(1,2),F(-1),F(1,2)]]
action=[[sum(coeffs[j][i]*F(maps[i]**k) for i in range(3)) for k in range(3)] for j in range(3)]
assert action == [[F(int(i==j)) for i in range(3)] for j in range(3)]
for row in action: print(' '.join(str(a) for a in row))
print('PASS: degree-separated algebraic correspondences on elliptic E')
print('STOP: no universal algebraic correspondence construction for arbitrary X')