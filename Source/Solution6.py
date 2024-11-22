"""
fair 6  die
roll until 6
flip coin until head
pn = probability that you need a total of exactly n rolls and flips
find max (pns)
THIS CODE IS PURPOSELY NOT EFFICIENT RATHER IT IS VERY COMPACT AND PRIORITISES THE LEAST LINES
"""
prob  = lambda n: sum([((5/6)**(k-1) * (1/6)) * ((1/2)**(n-k-1) * (1/2)) for k in range(1, n)])
print(f"Answer is {max([prob(n) for n in range(2, 50)]):.6f}")
