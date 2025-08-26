import string

# Ciphertext
cipher = "HIHHJEOCEJJJWC"
alpha = string.ascii_uppercase

# Affine cipher keys
a = 23
b = 16

# Modular inverse of a under mod 26
a_inv = pow(a, -1, 26)

# Decryption: D(y) = a_inv * (y - b) mod 26
result = []
for ch in cipher:
    y = alpha.index(ch)
    x = (a_inv * (y - b)) % 26
    result.append(alpha[x])

plaintext = ''.join(result)
print("Decrypted text:", plaintext)
