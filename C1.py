def mod_steps(a, b):
    """
    Show the integer division and remainder for a % b, and return the remainder.
    """
    if b == 0:
        raise ValueError("Division by zero")
    q = a // b        # integer quotient
    r = a % b         # remainder
    print(f"{a} ÷ {b} = {q} with remainder {r}")
    print(f"{a} = {b} * {q} + {r}")
    return r

# Given values
r1 = mod_steps((pow(8,13)), 271)
print()  # blank line
r2 = mod_steps(pow(12,23), 973)

# final results
print("\nFinal results:")
print( r1)
print( r2)
