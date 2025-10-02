import math

# Function to calculate GCD using math.gcd
def find_gcd(a, b):
    return math.gcd(a, b)

# Given numbers
pairs = [(4105, 10), (4539, 6)]

for a, b in pairs:
    gcd_val = find_gcd(a, b)
    print(f"GCD of {a} and {b} = {gcd_val}")
