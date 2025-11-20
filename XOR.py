def xor_cipher(message, key):
    return ''.join(
        chr(ord(m) ^ ord(key[i % len(key)]))
        for i, m in enumerate(message)
    )

# Input message and key
message = "HELLO"
key = "KEY"

# Encrypt the message
encrypted = xor_cipher(message, key)
print("Encrypted Message:", encrypted)

# Decrypt the message
decrypted = xor_cipher(encrypted, key)
print("Decrypted Message:", decrypted)
