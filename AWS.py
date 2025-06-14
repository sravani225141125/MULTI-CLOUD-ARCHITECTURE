# Example AWS Python script
import boto3

def list_buckets():
    s3 = boto3.client('s3')
    for bucket in s3.list_buckets()['Buckets']:
        print(bucket['Name'])

list_buckets()
