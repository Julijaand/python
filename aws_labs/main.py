import boto3

# Create an S3 client
s3_client = boto3.client('s3')

# List all S3 buckets
response = s3_client.list_buckets()

# Extract bucket names from the response
bucket_names = [bucket['Name'] for bucket in response['Buckets']]

# Print the list of bucket names
print("List of S3 Buckets:")
for bucket_name in bucket_names:
    print(bucket_name)
