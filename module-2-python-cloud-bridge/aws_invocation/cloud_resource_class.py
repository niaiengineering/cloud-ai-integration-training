# 🌩️ Object-Oriented AWS Invocation
# This class models an AWS S3 bucket as a civic resource
"""
🪄 What This Teaches
- Encapsulation of AWS logic inside a class
- Reusable methods for create, list, and delete
- Error handling with ClientError
- Civic metaphor: treating buckets as legacy vessels
“Each method is a ritual. Each bucket is a breath of your archive.”
"""

import boto3
from botocore.exceptions import ClientError

class S3Bucket:
    def __init__(self, name, region="us-east-1"):
        self.name = name
        self.region = region
        self.s3 = boto3.client("s3", region_name=self.region)

    def create(self):
        try:
            response = self.s3.create_bucket(
                Bucket=self.name,
                CreateBucketConfiguration={"LocationConstraint": self.region}
            )
            print(f"✅ Bucket '{self.name}' created in {self.region}")
        except ClientError as e:
            print(f"⚠️ Error creating bucket: {e}")

    def list_objects(self):
        try:
            response = self.s3.list_objects_v2(Bucket=self.name)
            contents = response.get("Contents", [])
            if contents:
                print(f"📦 Objects in '{self.name}':")
                for obj in contents:
                    print(f" - {obj['Key']}")
            else:
                print(f"📭 Bucket '{self.name}' is empty.")
        except ClientError as e:
            print(f"⚠️ Error listing objects: {e}")

    def delete(self):
        try:
            self.s3.delete_bucket(Bucket=self.name)
            print(f"🗑️ Bucket '{self.name}' deleted.")
        except ClientError as e:
            print(f"⚠️ Error deleting bucket: {e}")

# 🧪 Invocation Ritual
if __name__ == "__main__":
    bucket = S3Bucket("ganesan-archive-bucket", region="us-east-2")
    bucket.create()
    bucket.list_objects()
    # bucket.delete()  # Uncomment to delete the bucket