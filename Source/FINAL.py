"""
tri
a  = 2024
b
c  = hyp
integer units

N values for b and smallest is B

find N*B
90 10 900 [90, 1407, 1518, 1632, 2415, 3795, 3990, 5382, 5643, 8343, 11040, 11550,22218, 23232,44505, 46530]
"""

tri = lambda b, c: b > 0 and c > 0 and 2024**2 + b**2 == c**2
N = [90, 1407, 1518, 1632, 2415, 3795, 3990, 5382, 5643, 8343, 11040, 11550,22218, 23232, 44505, 46530]
[[ N.append(b) if tri(b,c) else None for c in range(50000, 60000)] for b in range(50000,60000)]
ans = min(N) * len(N)
print(f"{min(N)} {len(N)} {ans} {N}")

""""""