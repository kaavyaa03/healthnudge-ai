import os
import boto3

# AWS S3 configuration
bucket_name = "healthnudge-datasets"
local_folders = {
    "split_clinical_notes": "data/split_clinical_notes",
    "split_pubmedqa": "data/split_pubmedqa"
}

s3 = boto3.client("s3")

def upload_folder(local_path, s3_prefix):
    for root, _, files in os.walk(local_path):
        for file in files:
            local_file = os.path.join(root, file)
            s3_key = os.path.join(s3_prefix, os.path.relpath(local_file, local_path)).replace("\\", "/")
            print(f"Uploading {local_file} → s3://{bucket_name}/{s3_key}")
            s3.upload_file(local_file, bucket_name, s3_key)
    print(f"Uploaded folder '{s3_prefix}' to S3.")

if __name__ == "__main__":
    for prefix, folder in local_folders.items():
        if os.path.exists(folder):
            upload_folder(folder, prefix)
        else:
            print(f"Folder not found: {folder}")