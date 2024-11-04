"""
@GAURAV SHUKLA
Code Notes:
product(range(1, 7), repeat=5): Generates every possible sequence of five dice rolls, simulating all outcomes of rolling a six-sided die five times.
combinations(rolls, 3): From each set of five rolls, it generates all possible unique triplets to check for valid triangle side lengths.
"""
from itertools import product, combinations
valid = lambda a, b, c: (a + b > c) and (a + c > b) and (b + c > a)
total_outcomes ,no_tri = sum([ 1 for _ in product(range(1, 7), repeat=5)]),sum([1 if (not(any(valid(a, b, c) for a, b, c in combinations(rolls, 3)))) else 0 for rolls in product(range(1, 7), repeat=5)])
print(f"Answer: {(no_tri / total_outcomes):.4f}")