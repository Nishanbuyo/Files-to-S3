import os
import requests
import boto3
import files_sdk
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Files.com configuration
FILES_COM_API_KEY = os.getenv("FILES_COM_API_KEY")
FILES_COM_BASE_URL = os.getenv("FILES_COM_BASE_URL")

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")

# Files.com configuration
files_sdk.set_api_key(FILES_COM_API_KEY)
files_sdk.base_url = FILES_COM_BASE_URL

# S3 configuration
s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
)


# Function to upload a file to S3
def upload_file_to_s3(file_path, s3_key):
    """Uploads a file from Files.com to S3."""
    try:
        with open(file_path, "rb") as f:
            s3_client.upload_fileobj(f, S3_BUCKET_NAME, s3_key)
            print(f"File uploaded to S3: {S3_BUCKET_NAME}/{s3_key}")
    except Exception as e:
        print(f"Error uploading file: {str(e)}")


def download_file(item, local_file_path):
    try:
        downloaded_file = files_sdk.file.download(item.path, local_file_path)
        download_url = downloaded_file.download_uri

        response = requests.get(download_url)
        response.raise_for_status()

        with open(local_file_path, "wb") as f:
            f.write(response.content)

        print(f"File downloaded to: {local_file_path}")

    except Exception as e:
        print(f"Error downloading file {item.path}: {e}")


# Function to download a file from Files.com
def list_files_and_folders_recursive(path, local_base_path):
    try:
        for item in files_sdk.folder.list_for(path).auto_paging_iter():
            local_path = os.path.join(local_base_path, item.path.lstrip("/"))

            if item.type == "directory":
                os.makedirs(local_path, exist_ok=True)
                list_files_and_folders_recursive(item.path, local_base_path)

            elif item.type == "file":
                os.makedirs(os.path.dirname(local_path), exist_ok=True)
                print(f"Downloading file to: {local_path}")
                download_file(item, local_path)
                s3_key = item.path.lstrip("/")
                upload_file_to_s3(local_path, s3_key)

    except Exception as e:
        print(f"Error: {str(e)}")


# Example usage
if __name__ == "__main__":
    root_path = "/analytics_sftp/analytics_db/"
    local_download_base = "downloads"
    os.makedirs(local_download_base, exist_ok=True)
    list_files_and_folders_recursive(root_path, local_download_base)
