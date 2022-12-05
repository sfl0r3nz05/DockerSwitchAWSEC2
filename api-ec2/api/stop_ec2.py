#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import json
import time
import logging
import boto3.ec2
from botocore.exceptions import ClientError
from flask import Flask, jsonify, request, json

#def status(request):
def stop(id):
    """
    This code is from Amazon's EC2 example.
    Do a dryrun first to verify permissions.
    Try to get the EC2 instance status.
    """
    
    try:
        region_name_var=os.environ.get("REGION_NAME")  #Recover region name from env variables
        ec2 = boto3.client('ec2', region_name=region_name_var)
        response = ec2.stop_instances(InstanceIds=[id], DryRun=False)
        if (response):
            return jsonify(response)
        else:
            resp = {'message': 'fail'}
            return jsonify(resp)
    except ClientError as e:
        print(e)
