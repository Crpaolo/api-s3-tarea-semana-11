import boto3
import json

def lambda_handler(event, context):
    body = json.loads(event["body"])
    bucket_name = body["bucket"]

    s3 = boto3.client("s3")

    try:
        s3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={
                'LocationConstraint': 'us-east-1'
            }
        )
        
        return {
            "statusCode": 200,
            "message": f"Bucket '{bucket_name}' creado correctamente."
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "error": str(e)
        }
