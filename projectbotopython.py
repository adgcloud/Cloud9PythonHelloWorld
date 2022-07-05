#!/usr/bin/env python3.7
import boto3

ec2 = boto3.resource("ec2")

for instance in ec2.instances.all():
    if instance.id == "i-0c870707a894bbc1a":
        print("cloud9instance", ec2.Instance(instance.id),instance.id)
    else:
        print("not cloud9 instance", ec2.Instance(instance.id),instance.id)
        #ec2.Instance(instance.id).stop()