import base64

def to_base64(text):
    """Convert text to Base64 encoded string."""
    return base64.b64encode(text.encode("utf-8")).decode("utf-8")

def to_hex(text):
    """Convert text to Hexadecimal string."""
    return text.encode("utf-8").hex()

# --- Example usage ---
strings = [
    "hello",
    "Hello",
    "HELLO"
]

print("Original String   |   Base64 Value   |   Hex Value")
print("-" * 60)

for s in strings:
    base64_val = to_base64(s)
    hex_val = to_hex(s)
    print(f"{s:<16} | {base64_val:<15} | {hex_val}")
