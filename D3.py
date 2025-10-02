import random

def is_prime(n, k=5):
    """Miller-Rabin primality test."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # write n-1 as 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

# Define ranges
ranges = [100, 1000, 5000, 10000]

# Find the highest prime for each range
for n in ranges:
    for candidate in range(n, 1, -1):  # start from n and go down
        if is_prime(candidate):
            print(f"Highest prime ≤ {n}: {candidate}")
            break
