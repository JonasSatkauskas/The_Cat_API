import json
import boto3


def lambda_handler(event, context):
    # Instanciating connection objects with DynamoDB using boto3 dependency
    dynamodb = boto3.resource('dynamodb')
    
    # Getting the table the table object
    cats = dynamodb.Table('CATS')
    
    catID = event['cat_id']
    catName = event['name']

    # Putting a try/catch to log to user when some error occurs
    try:
        cats.put_item(
           Item={     
                'cat_id': catID,
                'name': catName
                
            }
        )
        return {
            'statusCode': 200,
            'body': json.dumps(f'{catName} goes inside!')
        }
    except:
        print('Closing lambda function')
        return {
                'statusCode': 400,
                'body': json.dumps(f"{catName} did not go inside because it couldn't find the way in!")
        }