def is_prime(n):
    """Check if n is a prime number."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    # check possible divisors up to sqrt(n)
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Generate primes up to 100
primes = [2, 3]  # start with the first two primes
for k in range(1, 100):
    for candidate in [6 * k - 1, 6 * k + 1]:
        if candidate <= 100 and is_prime(candidate):
            primes.append(candidate)

print("Prime numbers up to 100:")
print(sorted(primes))
