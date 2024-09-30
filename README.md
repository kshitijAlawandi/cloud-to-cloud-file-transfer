# iCloud to Local and OneDrive Uploader

This project consists of Python scripts that allow users to download photos from iCloud and upload files to OneDrive. The project handles user credentials securely by encrypting them and provides an easy way to manage files between cloud storage and local systems.

## Project Structure

```
project_directory/
│
├── cloud2local.py          # Script to download photos from iCloud to a local directory
├── credentials_manager.py   # Handles credential encryption and storage
├── local2drive.py          # Script to upload files from a local directory to OneDrive
├── config.json             # Configuration file containing paths and access tokens
└── .gitignore              # Specifies files to ignore in Git
```

## Prerequisites

- Python 3.x
- `pyicloud` library
- `cryptography` library
- `requests` library

You can install the required libraries using pip:

```bash
pip install pyicloud cryptography requests
```

## Configuration

Before running the scripts, you need to create a `config.json` file in the project directory with the following structure:

```json
{
    "download_folder": "path/to/download/folder",
    "access_token": "your_onedrive_access_token",
    "directory": "path/to/local/files"
}
```

- `download_folder`: The folder where photos will be downloaded from iCloud.
- `access_token`: The access token for OneDrive API authentication.
- `directory`: The local directory containing files to upload to OneDrive.

## Usage

### Downloading iCloud Photos

1. Run the `cloud2local.py` script:

   ```bash
   python cloud2local.py
   ```

2. Follow the prompts to enter your iCloud credentials. The script will handle two-factor authentication if required.

### Uploading Files to OneDrive

1. Run the `local2drive.py` script:

   ```bash
   python local2drive.py
   ```

This will upload all files from the specified local directory to your OneDrive.

## Security

- User credentials are encrypted and stored securely using the `cryptography` library.
- The `.gitignore` file ensures that sensitive files such as `credentials.json` and `secret.key` are not included in version control.

## To-Do

- The script does not handle large file uploads (>200 Mb).
- Update the script to delete from iCloud and local folder once the OneDrive upload is complete.
- Try to find another way to access OneDrive as the access token can expire. (Avoid using Azure App Registration and Azure Active Directory).
- Automate the scripts to run on bi-weekly or monthly basis so that iCloud is cleared out regularly.
- Add more scripts for other cloud-cloud transfers.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [PyiCloud](https://pypi.org/project/pyicloud/) - Python wrapper for iCloud services.
- [Cryptography](https://cryptography.io/en/latest/) - Python library for encryption.
- [Requests](https://docs.python-requests.org/en/master/) - Simple HTTP library for Python.
