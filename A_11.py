val = 41   # decimal value

print("Original (Dec):", val)
print("Original (Bin):", bin(val))

# Shift left
print("Left shift by 1:", val << 1, " (Bin:", bin(val << 1), ")")
print("Left shift by 2:", val << 2, " (Bin:", bin(val << 2), ")")

# Shift right
print("Right shift by 1:", val >> 1, " (Bin:", bin(val >> 1), ")")
print("Right shift by 2:", val >> 2, " (Bin:", bin(val >> 2), ")")
