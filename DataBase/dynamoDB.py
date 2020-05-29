import boto3
import logging


class Database:
    def __init__(self):
        self.dynamo_client = boto3.resource('dynamodb', endpoint_url='http://dynamodb-local:8000/')

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

    def read_all_item(self, table_name):
        table = self.dynamo_client.Table(table_name)
        response = table.scan()
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

if __name__ == '__main__':
    db = Database()
    #db.create_table("user-info")

    # res = db.read_item("user-info", "id", "1111")
    # print(res["Item"]["id"])
    # item = {"id": "8888", "email": "hi@gmail.com", "name": "mina", "authenticated":False}
    # db.add_item("user-info", item)
    # #
    # res2 = db.read_item("user-info", "8888",  "hi@gmail.com")
    # print(res2) #["Item"]["id"], res2["Item"]["email"], res2["Item"]["name"]
    # item2 = {"id": "23445", "email": "hehe@gmail.com", "password": 1234}
    # db.add_item("user-info", item2)
    item = {"id": "8888", "email": "hi@gmail.com", "name": "mina", "authenticated":False}
    db.add_item("user-info", item)
    res2 = db.read_item("user-info", "8888")
    print(res2)
    res3 = db.read_all_item("user-info")
    print(res3)


## docker-compose -f docker-compose.yaml up -d


## docker run -d -p 8000:8000 amazon/dynamodb-local
## docker run -p 8000:8000 -v my-volume:/dbstore amazon/dynamodb-local -jar DynamoDBLocal.jar -sharedDb -dbPath /dbstore
