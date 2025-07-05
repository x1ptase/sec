def caesar_encrypt(text, shift):
    result=""
    for char in text:
        if char.isalpha():
            ascii_offset=65 if char.isupper() else 97
            result+=chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

text="Hello, World!"
shift=3
encrypted=caesar_encrypt(text, shift)
decrypted=caesar_decrypt(encrypted, shift)

print(f"Original: {text}")
print(f"Encrypted (shift={shift}): {encrypted}")
print(f"Decrypted: {decrypted}")