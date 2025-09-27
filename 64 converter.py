import base64

def to_base64(text):
    """
    Convert text into Base64 encoded string.
    """
    # Convert text into bytes
    text_bytes = text.encode('utf-8')
    
    # Encode bytes into Base64
    base64_bytes = base64.b64encode(text_bytes)
    
    # Convert Base64 bytes to string
    return base64_bytes.decode('utf-8')

def from_base64(base64_string):
    """
    Convert Base64 encoded string back to normal text.
    """
    base64_bytes = base64_string.encode('utf-8')
    text_bytes = base64.b64decode(base64_bytes)
    return text_bytes.decode('utf-8')

def to_hex(text):
    """
    Convert text into Hexadecimal string.
    """
    return text.encode('utf-8').hex()

def from_hex(hex_string):
    """
    Convert Hexadecimal string back to normal text.
    """
    return bytes.fromhex(hex_string).decode('utf-8')


# Example usage
plain_text = input("Enter text: ")

# Convert to Base64 and Hex
base64_value = to_base64(plain_text)
hex_value = to_hex(plain_text)

print("\n--- Encoded Values ---")
print("Base64:", base64_value)
print("Hex   :", hex_value)

# Decode back to original
decoded_from_base64 = from_base64(base64_value)
decoded_from_hex = from_hex(hex_value)

print("\n--- Decoded Values ---")
print("From Base64:", decoded_from_base64)
print("From Hex   :", decoded_from_hex)
