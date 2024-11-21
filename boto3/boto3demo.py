import boto3

# client = boto3.client('s3')

# response = client.create_bucket(
#     Bucket='sairaja-demo-bucket-123'
# )
# print(response)

# client = boto3.client('s3')

# response= client.list_buckets()
# print(response['Buckets'])

# lambda_client= boto3.client('lambda')

# upload a file to s3 bucket
# client = boto3.client('s3')
# response = client.put_object(
#     Body=open("boto3/boto3demo.py","r").read(),
#     Bucket='sairaja-demo-bucket-123',
#     Key='index_1.py',
# )
# print(response)
# client = boto3.client('s3')
# response = client.get_object(
#     Bucket='sairaja-demo-bucket-123',
#     Key='index_1.py',
# )
# print(response.get("Body").read().decode())

#delete bucket
client = boto3.client('s3')
# response = client.delete_object(
#     Bucket='sairaja-demo-bucket-123',
#     Key='boto3/boto3demo.py',
# )
# print(response)

response = client.delete_bucket(
    Bucket='sairaja-demo-bucket-123',
)
