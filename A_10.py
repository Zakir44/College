import base64

s1 = "crypto"
s2 = "crypto1"

print("crypto  →", base64.b64encode(s1.encode()).decode())
print("crypto1 →", base64.b64encode(s2.encode()).decode())
