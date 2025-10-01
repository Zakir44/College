import base64

def from_base64(encoded):
    """Decode a Base64 string into ASCII text."""
    return base64.b64decode(encoded.encode("utf-8")).decode("utf-8")

def from_hex(encoded):
    """Decode a Hex string into ASCII text."""
    return bytes.fromhex(encoded).decode("utf-8")

# --- Example usage ---
base64_values = [
    "bGxveWRz"     
        
       
]

hex_values = [
    "6E6170696572 ",     
    "01000001 01101110 01101011 01101100 01100101 00110001 00110010 00110011",   
   
]

print("Decoding Base64 → ASCII")
for b64 in base64_values:
    print(f"{b64}  -->  {from_base64(b64)}")

print("\nDecoding Hex → ASCII")
for hx in hex_values:
    print(f"{hx}  -->  {from_hex(hx)}")
