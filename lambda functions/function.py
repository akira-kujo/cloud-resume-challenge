#codebase increments visitor count on DynamoDB table

#populate the table variable with the target dynamodb table
#grab the key (record_id) from the table and the item count
#retrieve the item from the table using a specified key
#extract visitor count from the item with variable visitor_count
#increment visitor_count by 1 each time the func is triggered
#print the visitor_count
#update the items within the table for the 'record_id' key
#updating the previous visitor_count with the incremented value

import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('visitor-table')

def lambda_handler(event, context):
    response = table.get_item(Key={
            'record_id':'0'
        })

    VisitorCount = response['Item']['VisitorCount']
    VisitorCount = VisitorCount + 1
    print(VisitorCount)

    response = table.put_item(Item={
        'record_id':'0',
        'VisitorCount':VisitorCount
        })

    return VisitorCount