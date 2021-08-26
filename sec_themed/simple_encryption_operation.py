#
# This will be a simple encryption test by using the following approach:
#
# Keysize:              K is 32bit
# Message:              M will be splitted into 32bit chunks
# Encryption Function:  We will use a 2x2 Matrix as presentation and each
#                       cell will cover 1 byte
#                       -> Substitution (mapping of bytes)
#                       -> Mixing/Shifting Rows
#                       -> Repeating this 5 times
#
# Method 1 (ECB):
# Mn -> Ek -> Cn
#
# Method 2 (CBC):
# M0 XOR IV   -> Ek -> C0
# Mn XOR Mn-1 -> Ek -> Cn
#
#

# 4 bytes = 32bit
CHUNK_SIZE = 4
SECRET_KEY = b'kM4!'
IV = b'3MnB'

#
# Encryption / Description of 32bit sized chunks
# + some helper functions
#

def add_padding(chunks: bytearray) -> bytearray:
    # add padding if message is len(msg) mod 32 != 0
    if (len(chunks) % CHUNK_SIZE) == 0:
        return chunks
    chunks.append(1)
    while (len(chunks) % CHUNK_SIZE) != 0:
        chunks.append(0)
    return chunks


def xor(msg_a: bytes, msg_b: bytes) -> bytes:
    return bytes(a ^ b for a, b in zip(msg_a, msg_b))       

def encrypt(message: bytes, key=SECRET_KEY) -> bytes:
    """
    message is a 32bit chunk of the whole message
    """
    # Todo: This needs to be enchanced!
    return xor(message, key)

def decrypt(ciphertext: bytes, key=SECRET_KEY) -> bytes:
    # Todo: see encrypt, because it will be the inverse
    return xor(ciphertext, key)


#
# Electronic Code Book Implementation
#
def encrypt_ecb(message: bytes) -> bytes:
    encrypted_msg = b''
    msg_array = bytearray(message)
    # add padding to fill up all chunks to be 32bits
    msg_array = add_padding(msg_array)
    # encrypt each chunk with the same key function!   
    for i in range(0, len(msg_array), CHUNK_SIZE):
        ab = bytes(msg_array[i:i+CHUNK_SIZE])
        encrypted_msg += encrypt(ab)
    return encrypted_msg


def decrypt_ecb(ciphertext: bytes) -> bytes:
    decrypted_msg = b''
    msg_array = bytearray(ciphertext)
    for i in range(0, len(msg_array), CHUNK_SIZE):
        ab = bytes(msg_array[i:i+CHUNK_SIZE])
        decrypted_msg += decrypt(ab)

    # cut the padding
    i = 0
    msg_len = len(msg_array)
    pad_pos = msg_len
    pad_started = False
    for byte in decrypted_msg:
        if byte == 1:
            pad_started = True
            pad_pos = i
        elif byte != 0 and pad_started:
            pad_started = False
            pad_pos = msg_len
        i +=1

    return decrypted_msg[0:pad_pos]

#
# Cipher Block Chaining Implementation
#
def encrypt_cbc(message: bytes) -> bytes:
    last_ciphertext = IV
    encrypted_msg = b''
    msg_array = bytearray(message)
    # add padding to fill up all chunks to be 32bits
    msg_array = add_padding(msg_array)
    # encrypt each chunk with the same key function!
    for i in range(0, len(msg_array), CHUNK_SIZE):
        chunk = bytes(msg_array[i:i+CHUNK_SIZE])
        # encrypt first with iv | last cipher
        cipher_chunk = xor(chunk, last_ciphertext)
        # encrypt then with key
        last_ciphertext = encrypt(cipher_chunk)
        encrypted_msg += last_ciphertext

    return encrypted_msg


def decrypt_cbc(ciphertext: bytes) -> bytes:
    last_ciphertext = IV
    decrypted_msg = b''
    msg_array = bytearray(ciphertext)
    for i in range(0, len(msg_array), CHUNK_SIZE):
        chunk = bytes(msg_array[i:i+CHUNK_SIZE])
        cipher_chunk = decrypt(chunk)
        decrypted_msg += xor(cipher_chunk, last_ciphertext)        
        last_ciphertext = chunk

    # cut the padding
    i = 0
    msg_len = len(msg_array)
    pad_pos = msg_len
    pad_started = False
    for byte in decrypted_msg:
        if byte == 1:
            pad_started = True
            pad_pos = i
        elif byte != 0 and pad_started:
            pad_started = False
            pad_pos = msg_len
        i +=1

    return decrypted_msg[0:pad_pos]



def main():

    message = b'You can see the Pattern Pattern Pattern Pattern !!!!'

    print("ECB Implementation")

    print(message)
    ciphertext = encrypt_ecb(message)
    print(ciphertext)
    message_1 = decrypt_ecb(ciphertext)
    print(message_1)

    print("\n---\n")
    print("CBC Implementation")

    print(message)
    ciphertext = encrypt_cbc(message)
    print(ciphertext)
    message_1 = decrypt_cbc(ciphertext)
    print(message_1)


if __name__ == "__main__":
    main()