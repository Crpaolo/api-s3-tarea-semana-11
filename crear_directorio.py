import boto3
import json

def lambda_handler(event, context):
    body = json.loads(event["body"])
    bucket = body["bucket"]
    directorio = body["directorio"]  # ejemplo: "imagenes/"

    s3 = boto3.client("s3")

    try:
        s3.put_object(
            Bucket=bucket,
            Key=f"{directorio}/"  # key vacía para crear prefijo
        )

        return {
            "statusCode": 200,
            "message": f"Directorio '{directorio}' creado en bucket '{bucket}'."
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "error": str(e)
        }
