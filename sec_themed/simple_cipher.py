

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


text = "Das ist ein Test"
print(f"Initial: {text}")
encrypted = encrypt(text, 7)
print(f"Encrypted: {encrypted}")
decrypted = decrypt(encrypted, 7)
print(f"Decrypted: {decrypted}")