import string
import secrets
import re

special_chars = '?+!#'
dictionary = string.ascii_letters + string.digits + special_chars

def validate_passwd(passwd) -> bool:
    return (bool(re.search("[a-z]", passwd)) and
            bool(re.search("[A-Z]", passwd)) and 
            bool(re.search("[0-9]", passwd)) and 
            bool(re.search("[?+!#]", passwd)))

def get_random_char() -> str:
    return secrets.choice(dictionary)

def _gen_passwd(length) -> str:
    return ''.join([get_random_char() for i in range(0,length)])

def gen_passwd(length=8) -> str:
    if length < 4:
        raise Exception("Password must have a length of 4 characters or more!")
    passwd = _gen_passwd(length)
    i = 0
    while not validate_passwd(passwd):
        passwd = _gen_passwd(length)
    return passwd


def main():
    print("Print 5 passwords")
    for i in range(0,5):
        print(f"Password Nr.{i+1}: {gen_passwd(22)}")


if __name__ == "__main__":
    main()