import boto3

client=boto3.client("ec2")
x = client.describe_vpcs()
no_of_vpcs=x["Vpcs"]
vpccount = len(no_of_vpcs)
print(vpccount)