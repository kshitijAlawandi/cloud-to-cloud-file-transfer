import json
import os
from cryptography.fernet import Fernet
from getpass import getpass

# Generate and store an encryption key if it doesn't exist
def generate_key():
    if not os.path.exists("secret.key"):
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)

# Load the encryption key
def load_key():
    return open("secret.key", "rb").read()

# Encrypt and store credentials if they don't exist
def encrypt_and_store_credentials():
    if not os.path.exists("credentials.json"):
        username = input("Enter your iCloud username (Apple ID): ")
        password = getpass("Enter your iCloud password: ")
        credentials = {"username": username, "password": password}

        key = load_key()
        fernet = Fernet(key)
        encrypted_credentials = fernet.encrypt(json.dumps(credentials).encode())

        with open("credentials.json", "wb") as file:
            file.write(encrypted_credentials)
        print("Credentials encrypted and stored successfully.")
    else:
        print("Encrypted credentials already exist.")

# Decrypt and load credentials
def decrypt_credentials():
    key = load_key()
    fernet = Fernet(key)
    with open("credentials.json", "rb") as file:
        encrypted_credentials = file.read()
    decrypted_credentials = fernet.decrypt(encrypted_credentials)
    return json.loads(decrypted_credentials)
