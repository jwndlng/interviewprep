import string
import secrets
import re

def get_random_lowercase():
    return string.ascii_lowercase[secrets.randbelow(26)]

def get_random_uppercase():
    return string.ascii_uppercase[secrets.randbelow(26)]

def get_random_number():
    return str(secrets.randbelow(10))

def get_random_specialchar():
    special_chars = ['?', '+', '!', '#']
    return special_chars[secrets.randbelow(4)]

def contains_lowercase(passwd) -> bool:
    return bool(re.search("[a-z]", passwd))

def contains_uppercase(passwd) -> bool:
    return bool(re.search("[A-Z]", passwd))

def contains_numeric(passwd) -> bool:
    return bool(re.search("[0-9]", passwd))

def contains_specialchar(passwd) -> bool:
    return bool(re.search("[?+!#]", passwd))

def validate_passwd(passwd) -> bool:
    if not contains_lowercase(passwd):return False
    if not contains_uppercase(passwd):return False
    if not contains_numeric(passwd):return False
    if not contains_specialchar(passwd):return False
    return True

def get_random_char() -> str:
    a = {
        0: get_random_number(),
        1: get_random_lowercase(),
        2: get_random_uppercase(),
        3: get_random_specialchar()
    }
    return a[secrets.randbelow(4)]

def _gen_passwd(length) -> str:
    return ''.join([get_random_char() for i in range(0,length)])

def gen_passwd(length=8) -> str:
    if length < 4:
        raise Exception("Password must have a length of 4 characters or more!")
    passwd = _gen_passwd(length)
    while not validate_passwd(passwd):
        passwd = _gen_passwd(length)
    return passwd


def main():
    print("Print 5 passwords")
    for i in range(0,5):
        print(f"Password Nr.{i+1}: {gen_passwd(22)}")


if __name__ == "__main__":
    main()