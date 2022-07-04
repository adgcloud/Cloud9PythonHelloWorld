import boto3

aws_resource=boto3.resource("s3")
bucket=aws_resource.Bucket("morphintimebucket")
response = bucket.create(
    ACL='public-read',
)