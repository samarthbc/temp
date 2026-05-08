https://www.notion.so/ADA-Lab-1fec2b82643b80f59332f8b57146d4ae?source=copy_link

https://chatgpt.com/share/69fcb038-4014-83a4-8717-194d3a05e925


import boto3

ec2 = boto3.client('ec2')

def lambda_handler(event, context):

    instances = ec2.describe_instances(
        Filters=[
            {
                'Name': 'tag:AutoStop',
                'Values': ['True']
            },
            {
                'Name': 'instance-state-name',
                'Values': ['running']
            }
        ]
    )

    instance_ids = []

    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_ids.append(instance['InstanceId'])

    if instance_ids:
        ec2.stop_instances(InstanceIds=instance_ids)
        print("Stopping instances:", instance_ids)

    return {
        'statusCode': 200,
        'body': 'Instances stopped successfully'
    }
