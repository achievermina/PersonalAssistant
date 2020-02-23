import boto3
import json

class database:
    def __init__(self):
        self.dynamo_client = boto3.resource('dynamodb', endpoint_url='http://localhost:8042/')
        # self.response = self.dynamo_client.list_tables()

    def add_item(self, table_name, col_dict):
        table = self.dynamo_client.Table(table_name)
        response = table.put_item(Item=col_dict)
        return response


    def read_item(self, table_name, pk_name, pk_value):
        table = self.dynamo_client.Table(table_name)
        response = table.get_item(TableName=table_name,Key={'id':pk_value})
        return response

    def read_all_item(self, table_name):
        table = self.dynamo_client.Table(table_name)
        response = table.scan()
        return response


if __name__ == '__main__':
    db = database()
    res = db.read_item("user-info", "id", "1111")
    print(res["Item"]["id"])
    item = { "id": "8888", "email":"hi@gmail.com"}
    db.add_item("user-info", item)
    res2 = db.read_item("user-info", "id", "8888")
    print(res2["Item"]["id"], res2["Item"]["email"])

    res3 = db.read_all_item("user-info")
    print(res3)



## docker-compose -f docker-compose-dynamodb-local.yaml up -d
## docker run -d -p 8000:8000 amazon/dynamodb-local
## docker run -p 8000:8000 -v my-volume:/dbstore amazon/dynamodb-local -jar DynamoDBLocal.jar -sharedDb -dbPath /dbstore
