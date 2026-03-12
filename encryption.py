from cryptography.fernet import Fernet
import os



def load_key():
    if not os.path.exists('secret.key'):
        key = Fernet.generate_key()

        with open('secret.key',"wb") as f:
            f.write(key)

    else:
        with open('secret.key',"rb") as f:
            key = f.read()
    return key


def encrypt(password):
    token = f.encrypt(password.encode())
    return token


def decrypt(password):
    token = f.decrypt(password.encode())
    return token.decode()


KEY = load_key()
f = Fernet(KEY)
