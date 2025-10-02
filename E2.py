# LCG parameters
a = 22
c = 31
m = 100
seed = 35
n_terms = 4

sequence = []
x = seed

for _ in range(n_terms):
    x = (a * x + c) % m
    sequence.append(x)

print("First four numbers of the sequence:", sequence)
