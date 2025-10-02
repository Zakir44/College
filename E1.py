# LCG parameters
a = 21
c = 31
m = 100
seed = 35
n_terms = 5  # number of terms to generate

sequence = []
x = seed

for _ in range(n_terms):
    x = (a * x + c) % m
    sequence.append(x)

print("Generated sequence:", sequence)

# Expected sequence
expected = [66, 17, 88, 79, 90]
print("Does it match the expected sequence?", "Yes" if sequence == expected else "No")
