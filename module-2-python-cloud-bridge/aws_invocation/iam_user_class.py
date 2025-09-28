# 🛡️ Object-Oriented IAM Invocation
# This class models an AWS IAM user as a civic steward
"""
🪄 What This Teaches
- Encapsulation of IAM logic
- Modular methods for create, attach policy, and delete
- Civic metaphor: IAM users as contributors with scoped permissions
- Reinforces reproducibility and onboarding clarity
“Each IAM user is a steward—granted access with intention and reverence.”
"""

import boto3
from botocore.exceptions import ClientError

class IAMUser:
    def __init__(self, username):
        self.username = username
        self.iam = boto3.client("iam")

    def create(self):
        try:
            response = self.iam.create_user(UserName=self.username)
            print(f"✅ IAM user '{self.username}' created.")
        except ClientError as e:
            print(f"⚠️ Error creating IAM user: {e}")

    def attach_policy(self, policy_arn):
        try:
            self.iam.attach_user_policy(
                UserName=self.username,
                PolicyArn=policy_arn
            )
            print(f"🔐 Policy attached to '{self.username}': {policy_arn}")
        except ClientError as e:
            print(f"⚠️ Error attaching policy: {e}")

    def delete(self):
        try:
            self.iam.delete_user(UserName=self.username)
            print(f"🗑️ IAM user '{self.username}' deleted.")
        except ClientError as e:
            print(f"⚠️ Error deleting IAM user: {e}")

# 🧪 Invocation Ritual
if __name__ == "__main__":
    user = IAMUser("legacy-contributor")
    user.create()
    # Example policy: AmazonS3ReadOnlyAccess
    user.attach_policy("arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess")
    # user.delete()  # Uncomment to delete the user