# If a cat is microchiped, you can add a "completed" status next to it.
import boto3
import json


def lambda_handler(event, context):
    table = boto3.resource('dynamodb').Table('CATS')
    
    catID = event['cat_id']
    catName = event['name']
    fur = event['fur_color']
    
    response = table.get_item(Key={'cat_id': catID,
                                   'name': catName})

    item = response['Item']   
    item['fur_color'] = fur
     
    table.put_item(Item=item)
    
    return {
            'statusCode': 200,
            'body': json.dumps(f'{catName} was updated!')
        }
