def factors(n):
    """
    Return a sorted list of all positive integer factors of n.
    """
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    return result

# Example usage
num = 432
factor_list = factors(num)
print(f"The factors of {num} are:\n{factor_list}")
