# LCG parameters
a = 2_175_143
c = 10_653
m = 1_000_000
seed = 3553
n_terms = 4

sequence = []
x = seed

for _ in range(n_terms):
    x = (a * x + c) % m
    sequence.append(x)

print("First four numbers of the sequence:", sequence)
