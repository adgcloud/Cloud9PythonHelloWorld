import boto3
client=boto3.client("ec2")
response = client.delete_vpc(
    VpcId='vpc-0ebb59a81d67d9d06'
    )
    
print(response)