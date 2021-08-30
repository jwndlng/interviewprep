from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

def rsa_usage(msg):
    # keys
    key_pair = RSA.generate(1024)
    pub_key = key_pair.publickey()

    # msg
    print("---\nRSA TEST\n")
    print(f"RSA Initial Message: {msg}")

    # encryption
    encryptor = PKCS1_OAEP.new(pub_key)
    enc_msg = encryptor.encrypt(msg)
    print(f"RSA Encrypted Message: {binascii.hexlify(enc_msg)}")

    # decryption
    decryptor = PKCS1_OAEP.new(key_pair)
    dec_msg = decryptor.decrypt(enc_msg)
    print(f"RSA Decrypted Message: {dec_msg}")
    print("\n---")


def aes_usage():
    raise NotImplementedError


def main():
    rsa_usage(b'Secret Message!')


if __name__ == '__main__':
    main()