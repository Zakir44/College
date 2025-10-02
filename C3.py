# Loop through all given cases
cases = [
    {"message": 5, "e": 5, "p": 53, "expected": 51},
    {"message": 4, "e": 11, "p": 79, "expected": 36},
    {"message": 101, "e": 7, "p": 293, "expected": 176}
]

for case in cases:
    message = case["message"]
    e = case["e"]
    p = case["p"]
    expected = case["expected"]

    # Modular exponentiation
    cipher = (message ** e) % p
    print(f"Message={message}, e={e}, p={p} -> Cipher={cipher}", end=' ')
    print("Yes" if cipher == expected else "No")
