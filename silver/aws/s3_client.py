import boto3
import os

def get_s3_client():
    aws_access_key = dbutils.secrets.get(scope="aws-secrets", key="aws-access-key")
    aws_secret_key = dbutils.secrets.get(scope="aws-secrets", key="aws-secret-key")
    return boto3.client(
        's3',
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_key
    )
