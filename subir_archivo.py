import boto3
import json
import base64

def lambda_handler(event, context):
    body = json.loads(event["body"])

    bucket = body["bucket"]
    directorio = body["directorio"]
    filename = body["filename"]
    contenido = body["contenido"]   # base64 o texto

    s3 = boto3.client("s3")

    try:
        s3.put_object(
            Bucket=bucket,
            Key=f"{directorio}/{filename}",
            Body=contenido
        )

        return {
            "statusCode": 200,
            "message": f"Archivo '{filename}' subido correctamente."
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "error": str(e)
        }
