import requests
import os
import json

def upload_file_to_onedrive(access_token, file_path):
    # Get the file name and prepare the upload URL
    file_name = os.path.basename(file_path)
    upload_url = f"https://graph.microsoft.com/v1.0/me/drive/root:/{file_name}:/content"

    # Set up headers
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/octet-stream"
    }

    # Read the file and upload it
    with open(file_path, 'rb') as file:
        response = requests.put(upload_url, headers=headers, data=file)

    # Check if the upload was successful
    if response.status_code == 201:
        print(f"Uploaded {file_name} successfully!")
    else:
        print(f"Failed to upload {file_name}: {response.text}")

if __name__ == "__main__":
    with open('config.json') as config_file:
        config = json.load(config_file)
    # Get your access token here
    ACCESS_TOKEN = config["access_token"]
    directory = config["directory"]

    # Loop through each file in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            upload_file_to_onedrive(ACCESS_TOKEN, file_path)
