#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import time
import argparse
import boto3.ec2
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2')

class Mem:
    """
    Global Class Pattern:
    Declare globals here.
    """
    instance_id = ""

def stop():
    """
    This code is from Amazon's EC2 example.
    Do a dryrun first to verify permissions.
    Try to stop the EC2 instance.
    """
    print("------------------------------")
    print("Try to stop the EC2 instance.")
    print("------------------------------")

    try:
        ec2.stop_instances(InstanceIds=[Mem.instance_id], DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise

    # Dry run succeeded, call stop_instances without dryrun
    try:
        response = ec2.stop_instances(InstanceIds=[Mem.instance_id], DryRun=False)
        print(response)
    except ClientError as e:
        print(e)
