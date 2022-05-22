import boto3

instance_list = ['i-0bbfe65a7fe560d7a','i-0bbfe65a7fe560d7a','i-0bbfe65a7fe560d7a']

remove_dup_list = []

for i in set(instance_list):
    remove_dup_list.append(i)

print(type(remove_dup_list))
client = boto3.client('ec2')

add_tag = client.create_tags(
    DryRun=False,
    Resources=remove_dup_list,
    Tags=[{'Key': 'env','Value': 'dev'}])

if add_tag['ResponseMetadata']['HTTPStatusCode'] == 200:
    print("Ran successfully")



