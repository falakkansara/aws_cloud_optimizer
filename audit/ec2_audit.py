import boto3
import datetime 

ec2 = boto3.client('ec2')
cloudwatch = boto3.client('cloudwatch')

def list_instances():
    instances = []
    paginator = ec2.get_paginator('decribe_instances')
    for page in paginator.paginate():
        for reservation in page['Reservations']:
            for instance in reservation['Instances']:
                if instance['State']['Name'] == 'running':
                    instances.append({
                        'InstanceId': instance['InstanceId'], 
                        'InstanceType': instance['InstanceType']
                    })
    return instances 

def get_cpu_utilization(instance_id):
    now = datetime.datetime.now(datetime.UTC)
    start = now - datetime.timedelta(days=7)

    metrics = cloudwatch.get_metric_statistics(
        Namespace = 'AWS/EC2',
        MetricsName = 'CPUUtilization',
        Dimensions = [{'Name': 'InstanceId', 'Value': instance_id}],
        StartTime = start,
        EndTime = now,
        Period = 86400,
        Statistics = ['Average']
    )
    datapoints = metrics['Datapoints']
    if datapoints:
        return round(sum(dp['Average'] for dp in datapoints) / len(datapoints), 2)
    return None

def get_ec2_report():
    report = []
    for instance in list_instances():
        cpu = get_cpu_utilization(instance['InstaceId'])
        report.append({
            "instance_id": instance['InstanceId'],
            "type": instance['InstanceType'],
            "avg_cpu": cpu
        })
    return report 