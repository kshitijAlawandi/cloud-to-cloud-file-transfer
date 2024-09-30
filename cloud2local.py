import os
import json
from pyicloud import PyiCloudService
from credentials_manager import generate_key, encrypt_and_store_credentials, decrypt_credentials

def download_icloud_photos(download_folder):
    # Ensure encryption key and credentials are set up
    generate_key()  # Ensures the key is available
    encrypt_and_store_credentials()  # Prompts for credentials only if they don't exist

    # Load credentials from the encrypted file
    credentials = decrypt_credentials()
    username = credentials["username"]
    password = credentials["password"]

    # Create the download folder if it doesn't exist
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    # Login to iCloud
    api = PyiCloudService(username, password)

    # Check if two-factor authentication is required
    if api.requires_2fa:
        print("Two-factor authentication is required.")
        
        # Send the code to the trusted device (usually automatic)
        code = input("Enter the verification code you received: ")
        
        # Validate the provided verification code
        if not api.validate_2fa_code(code):
            print("Failed to verify the code.")
            return
        print("Two-factor authentication successful.")

    # Access the iCloud photo library
    photos = api.photos.all

    # Download photos
    for photo in photos:
        print(f"Downloading {photo.filename}...")
        with open(os.path.join(download_folder, photo.filename), 'wb') as file:
            file.write(photo.download().raw.read())
        print(f"{photo.filename} downloaded successfully.")

if __name__ == "__main__":
    with open('config.json') as config_file:
        config = json.load(config_file)
    download_folder = config["download_folder"]  # Change this to your desired folder path
    download_icloud_photos(download_folder)
