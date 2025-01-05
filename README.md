# Daniel Jewelers - Files to S3

This project is designed to upload files to Amazon S3 for Daniel Jewelers Files.com.

## Prerequisites

- AWS account with S3 access
- AWS CLI configured with appropriate credentials
- Python 3.x installed

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/daniel-jewelers-files-to-s3.git
    cd daniel-jewelers-files-to-s3
    ```

2. Install required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

## Configuration

1. Create a `.env` file in the root directory and add your AWS credentials and S3 bucket name:
    ```env
    AWS_ACCESS_KEY_ID=your_access_key_id
    AWS_SECRET_ACCESS_KEY=your_secret_access_key
    S3_BUCKET_NAME=your_bucket_name
    ```

## Usage

1. Run the script to upload files to S3:
    ```sh
    python files_to_s3.py
    ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries, please contact Nishan at nishan@example.com.
