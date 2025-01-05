# Daniel Jewelers - Files to S3

This project is designed to upload files to Amazon S3 for Daniel Jewelers Files.com.

## Prerequisites

- AWS account with S3 access
- AWS CLI configured with appropriate credentials
- Python 3.x installed
- Files.com with API access

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Nishanbuyo/Files-to-S3.git
    cd files-to-s3
    ```

2. Install required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

## Configuration

1. Create a `.env` file in the root directory and add your AWS credentials, S3 bucket name and Files credentials:
    ```env
    AWS_ACCESS_KEY_ID=your_access_key_id
    AWS_SECRET_ACCESS_KEY=your_secret_access_key
    S3_BUCKET_NAME=your_bucket_name

    FILES_COM_API_KEY = your_files_api_key
    FILES_COM_BASE_URL = 'https://files.teamsmc.io'
    ```

## Usage

1. Run the script to upload files to S3:
    ```sh
    python files_to_s3.py
    ```

