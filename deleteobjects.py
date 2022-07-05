import boto3

s3_resource=boto3.client("s3")

s3_resource.delete_object(Bucket="morphintimebucket", Key='testupload.txt')
