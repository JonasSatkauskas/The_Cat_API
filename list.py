import json
import boto3
from boto3.dynamodb.conditions import Key


def lambda_handler(event, context):
    dynamodb_client = boto3.client('dynamodb', region_name="us-east-2")
    try:
        response = dynamodb_client.query(
        TableName='CATS',
        KeyConditionExpression='cat_id = :cat_id',
        ExpressionAttributeValues={
            ':cat_id': {'S': '1'}
            }
        )
        return {    
            'statusCode': 200,    
            'body': response['Items']  
    }
    except:
        return {    
            'statusCode': 400,    
            'body': json.dumps(f"We could not retrieve these cats.")  
        }
