
# Delete the bucket
import boto3

# Create an S3 resource
s3_resource = boto3.resource('s3')

# Delete all S3 buckets
for bucket in s3_resource.buckets.all():
    try:
        for obj in bucket.objects.all():
            obj.delete()
        bucket.delete()
        print(f"Deleted bucket: {bucket.name}")
    except Exception as e:
        print(f"Error deleting bucket: {bucket.name}")
        print(f"Error message: {str(e)}")