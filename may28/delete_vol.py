

import boto3

client = boto3.client('ec2')

# response = client.delete_volume(
#     VolumeId='vol-0d8f7ee1b71a11550'
# )
response = client.describe_volumes()

#print(response['Volumes'][5])


for item_vol in response['Volumes']:
    if item_vol['SnapshotId'] == '':
        print(item_vol['VolumeId'] + ' - volume maked for deletion')