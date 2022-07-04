import boto3

resource=boto3.resource("s3")

bucket_list =list(resource.buckets.all())
len(bucket_list)


for bucket in bucket_list:
    print(bucket.name)