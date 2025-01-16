import boto3
import base64

def lambda_handler(event, context):
    try:
        
        file_content = event.get('file_content') 
        file_name = event.get('file_name') 
        bucket_name = event.get('bucket_name')  
        
        if not all([file_content, file_name, bucket_name]):
            return {
                'statusCode': 400,
                'body': 'file_content, file_name, and bucket_name are required.'
            }
        
        
        file_bytes = base64.b64decode(file_content)
        
       
        s3 = boto3.client('s3')
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=file_bytes)
        
        return {
            'statusCode': 200,
            'body': f'File {file_name} uploaded to {bucket_name} successfully.'
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }
