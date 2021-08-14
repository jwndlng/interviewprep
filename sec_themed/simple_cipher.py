

def encrypt(text, shift):
    charList = list(text)
    for i in range(0, len(text)):
        charList[i] = chr((ord(text[i]) + shift))
    return ''.join(charList)

def decrypt(text, shift):
    charList = list(text)
    for i in range(0, len(text)):
        charList[i] = chr((ord(text[i]) - shift))
    return ''.join(charList)


text = "This is a simple simple test"
print(f"Initial: {text}")
encrypted = encrypt(text, 7)
print(f"Encrypted: {encrypted}")
decrypted = decrypt(encrypted, 7)
print(f"Decrypted: {decrypted}")