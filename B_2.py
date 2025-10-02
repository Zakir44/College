import math

def is_coprime(a, b):
    return math.gcd(a, b) == 1

pairs = [(5435, 634), (5432, 634)]

for a, b in pairs:
    if is_coprime(a, b):
        print(f"{a} and {b}: Yes (they are co-prime)")
    else:
        print(f"{a} and {b}: No (they are not co-prime)")
