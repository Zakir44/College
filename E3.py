# LCG parameters
a = 954_365_343
c = 55_119_927
m = 1_000_000
seed = 436_241
n_terms = 4

sequence = []
x = seed

for _ in range(n_terms):
    x = (a * x + c) % m
    sequence.append(x)

print("First four numbers of the sequence:", sequence)
