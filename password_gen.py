import secrets
import string

def create_pw(pw_length=12):
    alphabet = string.ascii_letters + string.digits + string.punctuation

    while True:
        pwd = ''.join(secrets.choice(alphabet) for _ in range(pw_length))

        if (any(char in string.punctuation for char in pwd) and
                sum(char in string.digits for char in pwd) >= 2):
            return pwd


if __name__ == '__main__':
    print(create_pw())
