# src/upload_to_s3.py

import os
import boto3

# Replace with your actual bucket name
BUCKET_NAME = "healthnudge-datasets"

# Define folders to upload
folders = {
    "clinical_notes_raw": "data/clinical_notes_raw",
    "pubmedqa_raw": "data/pubmedqa_raw"
}

s3 = boto3.client("s3")

def upload_folder_to_s3(local_path, s3_prefix):
    for root, _, files in os.walk(local_path):
        for file in files:
            full_path = os.path.join(root, file)
            relative_path = os.path.relpath(full_path, local_path)
            s3_key = f"{s3_prefix}/{relative_path.replace(os.sep, '/')}"
            print(f"Uploading {s3_key}")
            s3.upload_file(full_path, BUCKET_NAME, s3_key)

for s3_prefix, folder_path in folders.items():
    upload_folder_to_s3(folder_path, s3_prefix)

print("Upload complete!")