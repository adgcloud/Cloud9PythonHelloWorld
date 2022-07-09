import boto3
ec2_client=boto3.client("ec2")
ec2_client.create_volume(AvailabilityZone='us-east-1f',
    Encrypted=True,
    Size=12,
    SnapshotId='snap-09081ec5cf2b35851',
    VolumeType='gp2')