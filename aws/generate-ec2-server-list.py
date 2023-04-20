#!/usr/bin/python

import json
import boto3
import os
from pathlib import Path
import datetime

ec2_info_file_path = Path('./ec2-info.json')
server_list_path = Path('./server-list.txt')
ACCESS_KEY = os.getenv('AWS_ACCESS_KEY_ID')
SECRET_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
SESSION_TOKEN = os.getenv('AWS_SESSION_TOKEN')
ec2 = boto3.client('ec2',
                   aws_access_key_id=ACCESS_KEY,
                   aws_secret_access_key=SECRET_KEY,
                   aws_session_token=SESSION_TOKEN
                   )

# Create instance's name list. As long, you have populated server-list.txt file, and you construct instances_name list
# the rest of the script will work.

# This logic can be adapted to Azure too using the python SDK. This will generate a Markdown table with the following
# columns: Instance Name | Image ID | Instance ID | Instance Type | Key Name | Launch Time | Private IP Address |
# Subnet ID | VPC ID, but you can add more columns if you want or remove some of them even more you can inset to an SQL
# database or a NoSQL database.

with open(server_list_path) as f:
    instances_name = f.read().splitlines()

filters = [{'Name': 'tag:Name', 'Values': instances_name}]


class DateTimeEncoder(json.JSONEncoder):
    def default(self, z):
        if isinstance(z, datetime.datetime):
            return str(z)
        else:
            return super().default(z)


def ec2_info():
    if ec2_info_file_path.is_file():
        print(f'File {ec2_info_file_path} exits')
    else:
        try:
            reservations = ec2.describe_instances(Filters=filters)
            with open(ec2_info_file_path, "w") as write_file:
                json.dump(reservations, write_file, cls=DateTimeEncoder, indent=4)
        except Exception as e:
            print(e)


ec2_info()

with open(ec2_info_file_path) as data_file:
    data = json.load(data_file)

group_list = []
instances_list = []
table_rows = ''
for item in data['Reservations']:
    group_list.append(item)

for instance in group_list:
    instances_list.append(instance['Instances'])

for e in instances_list:
    base_construct = e[0]
    ImageId = base_construct['ImageId']
    InstanceId = base_construct['InstanceId']
    InstanceType = base_construct['InstanceType']
    KeyName = base_construct['KeyName']
    LaunchTime = base_construct['LaunchTime']
    PrivateIpAddress = base_construct['PrivateIpAddress']
    SubnetId = base_construct['SubnetId']
    VpcId = base_construct['VpcId']
    Tags = base_construct['Tags']
    for tag in Tags:
        name_value = tag['Key'], tag['Value']
        if 'Name' in name_value:
            instance_name = name_value[1]
    # Construct a table row for this instance
    table_row = f"| {instance_name} | {ImageId} | {InstanceId} | {InstanceType} | {KeyName} | {LaunchTime} | {PrivateIpAddress} | {SubnetId} | {VpcId} |\n"
    table_rows += table_row

with open('SERVERS.md', 'a') as f:
    f.write(
        '| Instance Name | Image ID | Instance ID | Instance Type | Key Name | Launch Time | Private IP Address | Subnet ID | VPC ID |\n')
    f.write('| --- | --- | --- | --- | --- | --- | --- | --- | --- |\n')
    f.write(table_rows)

