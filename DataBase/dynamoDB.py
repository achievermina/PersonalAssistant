import boto3
import logging
import os
from dotenv import load_dotenv

load_dotenv()
DYNAMODB_ENDPOINT = os.getenv("DYNAMODB_ENDPOINT")

class Database:
    def __init__(self):
        self.dynamo_client = boto3.resource('dynamodb')

    def add_item(self, table_name, col_dict):
        table = self.dynamo_client.Table(table_name)
        response = table.put_item(Item=col_dict)
        logging.info("Adding a user in the database %s", response)

        return response

    def read_item(self, table_name, pk_value1):
        logging.info("reading item in database %s",pk_value1)
        try:
            table = self.dynamo_client.Table(table_name)
            response = table.get_item(Key={'id': pk_value1})
            return response['Item']
        except Exception as err:
            logging.error("Error: reading a user in the database %s", err)
            return None

    def update_item(self, table_name, key, attr, val):
        table = self.dynamo_client.Table(table_name)
        response = table.update_item(
            Key={
                'id': key
            },
            UpdateExpression='SET #attr1 = :val1',
            ExpressionAttributeNames={'#attr1': attr},
            ExpressionAttributeValues={':val1': val}
        )

        return response

    def create_table(self, table_name):
        table = self.dynamo_client.create_table(
            TableName= table_name,
            KeySchema=[
                {
                    'AttributeName': 'id',
                    'KeyType': 'HASH'  # Partition key
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'id',
                    'AttributeType': 'S'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 10
            }
        )

        print("Table status:", table.table_status)