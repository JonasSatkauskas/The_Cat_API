import json
import boto3
from boto3.dynamodb.conditions import Key


def lambda_handler(event, context):

    
    id = 0
    if 'cat_id' in event:
        id = event['cat_id']
        cat_list = id.split(',') 
        
    dynamodb_client = boto3.client('dynamodb', region_name="us-east-2")
    try:
        resp = []
        for i in cat_list:
            response = dynamodb_client.query(
            TableName='CATS',
            KeyConditionExpression='cat_id = :a',
            ExpressionAttributeValues={
                    ':a': {'S': i}
                    }
            )
            resp.append(response['Items'])
        
        return {    
            'statusCode': 200,    
            'body': resp
        }
        
    except:
        return {    
            'statusCode': 400,    
            'body': json.dumps(f"We could not retrieve these cats.")  
        }