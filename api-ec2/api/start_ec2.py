#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import time
import argparse
import boto3.ec2
from botocore.exceptions import ClientError

VERSION = '1.5.0'
ec2 = boto3.client('ec2')


class Mem:
    """
    Global Class Pattern:
    Declare globals here.
    """
    instance_id = ""

def start(request):
    """
    This code is from Amazon's EC2 example.
    Do a dryrun first to verify permissions.
    Try to start the EC2 instance.
    """
    print("------------------------------")
    print("Try to start the EC2 instance.")
    print("------------------------------")

    try:
        print("Start dry run...")
        ec2.start_instances(InstanceIds=[Mem.instance_id], DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise

    # Dry run succeeded, run start_instances without dryrun
    try:
        print("Start instance without dry run...")
        response = ec2.start_instances(InstanceIds=[Mem.instance_id], DryRun=False)
        print(response)
        fetch_public_ip()
    except ClientError as e:
        print(e)

