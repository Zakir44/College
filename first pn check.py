def is_prime(n):
    """
    Function to check if a number is prime.
    A prime number is greater than 1 and has no divisors other than 1 and itself.
    """
    if n <= 1:  # 0, 1, and negative numbers are not prime
        return False
    if n == 2:  # 2 is the only even prime number
        return True
    if n % 2 == 0:  # any other even number is not prime
        return False
    
    # Check divisors from 3 up to sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


# Example usage
num = int(input("Enter a number: "))
if is_prime(num):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")
