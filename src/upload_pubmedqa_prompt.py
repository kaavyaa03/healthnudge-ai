import boto3
import os

bucket_name = "healthnudge-datasets"
local_file = "data/pubmedqa_prompts.jsonl"
s3_key = "pubmedqa_prompts.jsonl"

s3 = boto3.client("s3")

def upload_file():
    if os.path.exists(local_file):
        print(f"Uploading {local_file} to s3://{bucket_name}/{s3_key} ...")
        s3.upload_file(local_file, bucket_name, s3_key)
        print("Upload complete.")
    else:
        print("File not found:", local_file)

if __name__ == "__main__":
    upload_file()