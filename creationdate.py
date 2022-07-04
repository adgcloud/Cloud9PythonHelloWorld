import boto3

#s3_resource=boto3.client??

s3_resource=boto3.client("s3")

buckets = s3_resource.list_buckets()["Buckets"][2]["Name"]
creation_date=s3_resource.list_buckets()["Buckets"][2]["CreationDate"]
#print(creation_date.strftime("%d%m%y_%H:%M:%s"))

for bucket in s3_resource.list_buckets()["Buckets"]:
    print(bucket["Name"])
    print(bucket["CreationDate"])
