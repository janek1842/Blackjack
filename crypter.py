import binascii
import hashlib
import os
import sqlite3
from cryptography.fernet import Fernet
import base64
import os

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """
    Load the previously generated key
    """
    return open("secret.key", "rb").read()

def changeGenerator():
    keyGenerator=False


def encrypt_message(message):
    """
    Encrypts a message
    """
    global keyGenerator

    if(not os.path.isfile('./secret.key')):
        generate_key()
    else:
        pass

    key = load_key()
    encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)
    return encrypted_message.decode()

def decrypt_message(encrypted_message):
    """
    Decrypts an encrypted message
    """
    encrypted_message = str(encrypted_message.fetchone()[0]).encode("utf-8")

    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    return decrypted_message.decode()
