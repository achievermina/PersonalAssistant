import boto3
import logging
import os
from dotenv import load_dotenv

load_dotenv()
DYNAMODB_ENDPOINT = os.getenv("DYNAMODB_ENDPOINT")

class Database:
    def __init__(self):
        self.dynamo_client = boto3.resource('dynamodb', endpoint_url=DYNAMODB_ENDPOINT)

    def add_item(self, table_name, col_dict):
        table = self.dynamo_client.Table(table_name)
        response = table.put_item(Item=col_dict)
        return response

    def read_item(self, table_name, pk_value1):
        logging.info("reading item in database %s",pk_value1)
        try:
            table = self.dynamo_client.Table(table_name)
            response = table.get_item(Key={'id': pk_value1})
            return response['Item']
        except Exception as err:
            logging.info("Error: reading a user in the database %s", err)
            return None

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

if __name__ == '__main__':
    db = Database()
    item = {"id": "8888", "email": "hi@gmail.com", "name": "mina", "email_verified":False}
    db.add_item("user-info", item)
    res2 = db.read_item("user-info", "8888")
    print(res2)
    res3 = db.read_all_item("user-info")
    print(res3)
