import boto3

ec2_client = boto3.resource('ec2')

instance = ec2_client.create_instances(
    ImageId='ami-0022f774911c1d690',
    InstanceType='t2.micro',
    KeyName='devops2-02',
    SecurityGroupIds=['sg-0293ff925a2137096','sg-01fbddc688fcd8dae'],
    SubnetId='subnet-f01f9b96',
    MaxCount=1,
    MinCount=1,
    TagSpecifications=[{'ResourceType':'instance','Tags':[{'Key':'Name','Value': 'created_by_python'}]}])