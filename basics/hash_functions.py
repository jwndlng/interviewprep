
#
# Using hashlib library!
#

import hashlib

def main():
    print(f"MD5 {hashlib.md5('test'.encode('utf-8')).hexdigest()}")
    print(f"SHA1 {hashlib.sha1(b'test').hexdigest()}")
    print(f"SHA256 {hashlib.sha256(b'test').hexdigest()}")

if __name__ == '__main__':
    main()