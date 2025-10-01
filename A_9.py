import base64

s = "crypto"
encoded = base64.b64encode(s.encode("utf-8"))
print(encoded.decode("utf-8"))
