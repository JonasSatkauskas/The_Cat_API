import json
import boto3


def lambda_handler(event, context):  
    dynamodb = boto3.resource('dynamodb')  
    catsTable = dynamodb.Table('CATS')  
    response = catsTable.scan()  
    return {    
        'statusCode': 200,    
        'body': response['Items']  
    }