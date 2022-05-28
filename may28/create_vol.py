import boto3

client = boto3.client('ec2')

response = client.create_volume(
    AvailabilityZone='us-east-1a',
    Encrypted=False,
    Size=1,
    VolumeType='gp3',
    DryRun=False
)

print(response['VolumeId'])
