#!/usr/bin/env python3.7
import boto3

ec2 = boto3.resource("ec2")
ec2.
for instance in ec2.instances.all():
    print(instance)