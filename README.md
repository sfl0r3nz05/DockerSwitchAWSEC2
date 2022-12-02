# Docker API to manage on/off AWS EC2 instances

- Creation of API based on Docker to manage AWS EC2 instances on/off.

## About

Start your Amazon Web Services EC2 Instance with Python 3:

    # Start EC2 instance
    python3 start_stop_ec2.py -u

    # Stop EC2 instance
    python3 start_stop_ec2.py -d

## Requirements

### Python Modules

If you never used [Amazon Web Services](https://aws.amazon.com/) with Python before, you have to install two additional modules:

    pip install boto3 botocore

or

    pip3 install boto3 botocore

### EC2 Instance ID

Enter your **EC2 ID** in a file with the name *instance_id.txt* and save this file in your Users/home folder:

    /home/[username]/instance_id.txt // Linux

 Check your EC2 dashboard for the available IDs.

### AWS Credentials

Save your **AWS Credentials** in your home/users folder:

Linux:

    /home/[username]/.aws

macOS:

    /Users/[username]/.aws

Windows:

    /Users/[username]/.aws

For more information about the content of the *.aws* folder check the AWS documentation: [Configuration and Credential Files](https://docs.aws.amazon.com/cli/latest/userguide/cli-config-files.html).

Instead of creating the *.aws* folder manually you can use the [AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/installing.html):

* [Installer for Windows](https://docs.aws.amazon.com/cli/latest/userguide/awscli-install-windows.html#install-msi-on-windows)
* [Installer for Linux, macOS, UNIX](https://docs.aws.amazon.com/cli/latest/userguide/awscli-install-bundle.html)

After you've installed the AWS CLI open the PowerShell (or the Command Prompt) in Windows. In UNIX-like systems open a Shell. Then run the following command:

    aws configure

Enter

* your AWS Access Key ID and
* your AWS Secret Access Key.
* As default region name enter your Availability Zone (AZ) and
* use "json" as default output format.

## Changelog

* 30/07/2017 - Receiving public IPv4 address
* 10/06/2018 - Added more print statements and updated `read_credentials()`. The path to your "instance_id.txt" is no longer hard coded.
* 29/11/2018 - Updated `parse_arguments()` and added more comments.

