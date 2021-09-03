import boto3
import json


def lambda_handler(event, context):
    
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('CATS')

    cat_id = event['cat_id']
    name = event['name']
    try:
        response = table.delete_item(
            Key={
                'cat_id': cat_id,
                'name': name
                
            },
        )
        print(f'A cat with ID {cat_id} has been deleted')
        
    except:
        print('Closing lambda function')
        print(event['cat_id'])
        print(cat_id)
        return {
                'statusCode': 400,
                'body': "We could not delete this id."
        }
    
    return response