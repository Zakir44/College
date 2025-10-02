def sieve_for_primes_to(n):
    """
    Generate all prime numbers up to n using the Sieve of Eratosthenes.
    """
    if n < 2:
        return []

    # Only odd numbers are considered, 2 is handled separately
    size = n // 2
    sieve = [1] * size
    limit = int(n ** 0.5)

    for i in range(1, limit):
        if sieve[i]:
            val = 2 * i + 1
            tmp = ((size - 1) - i) // val
            sieve[i + val::val] = [0] * tmp

    # Include 2 and remaining odd primes
    primes = [2] + [2 * i + 1 for i, v in enumerate(sieve) if v and i > 0]
    return primes

# Generate primes up to 1000
primes_up_to_1000 = sieve_for_primes_to(1000)

# Print the prime numbers
#

# Print the highest prime
print("\nHighest prime number generated:", max(primes_up_to_1000))
