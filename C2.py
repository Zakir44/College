def is_prime(n):
    """Check if n is a prime number."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def check_mod(M, p, expected):
    """Check M mod p and compare to expected."""
    if not is_prime(p):
        print(f"{p} is not prime!")
        return
    result = M % p
    print(f"{M} mod {p} = {result}")
    if result == expected:
        print("Yes")
    else:
        print("No")


# Given values
M = 85
p = 269
expected = 219

check_mod(M, p, expected)
