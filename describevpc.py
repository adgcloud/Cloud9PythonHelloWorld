import boto3

client=boto3.client("ec2")
describevpcs = client.describe_vpcs()
print(describevpcs)