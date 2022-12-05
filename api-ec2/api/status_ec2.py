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

#aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"), #Recover access key from env variables
#aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"), #Recover secret access key from env variables
#aws_session_token=os.environ.get("AWS_SESSION_TOKEN"), #Recover session token from env variables

#def status(request):
def status(id):
    """
    This code is from Amazon's EC2 example.
    Do a dryrun first to verify permissions.
    Try to get the EC2 instance status.
    """
    
    #try:
    #    region_name=os.environ.get("REGION_NAME")  #Recover region name from env variables
    #    aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"), #Recover access key from env variables
    #    aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"), #Recover secret access key from env variables
    #    aws_session_token=os.environ.get("AWS_SESSION_TOKEN"), #Recover session token from env variables
    #    ec2 = boto3.client('ec2', region_name=region_name, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, aws_session_token=aws_session_token)
    #    response = ec2.describe_instances()
    #    print(response)
    #    logging.info(response)
    #    if (response):
    #        return response
    #    else:
    #        resp = {'message': 'fail'}
    #        return jsonify(resp)
    #except ClientError as e:
    #    print(e)

    region_name=os.environ.get("REGION_NAME")  #Recover region name from env variables
    aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"), #Recover access key from env variables
    aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"), #Recover secret access key from env variables
    aws_session_token=os.environ.get("AWS_SESSION_TOKEN"), #Recover session token from env variables
    ec2 = boto3.client('ec2', region_name=region_name, aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, aws_session_token=aws_session_token)
    if (ec2):
        return ec2
    else:
        resp = {'message': 'fail'}
        return jsonify(resp)

