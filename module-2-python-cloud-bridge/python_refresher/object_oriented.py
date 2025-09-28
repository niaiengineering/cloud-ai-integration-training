# 🧪 Object-Oriented Invocation Ritual

class CloudResource:
    def __init__(self, name, resource_type):
        self.name = name
        self.resource_type = resource_type

    def describe(self):
        return f"{self.name} is a {self.resource_type} resource."

# Instantiate objects
s3_bucket = CloudResource("archive-bucket", "S3")
iam_user = CloudResource("legacy-steward", "IAM")

# Invoke methods
print(s3_bucket.describe())
print(iam_user.describe())