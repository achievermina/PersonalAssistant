import boto3

class database:
    def __init__(self, table_name):
        self.dynamo_client = boto3.client('dynamodb', endpoint_url='http://localhost:8000/')
        self.response = self.dynamo_client.list_tables()

    def add_item(self, table_name, col_dict):
        table = self.dynamo_client.Table(table_name)
        response = table.put_item(Item=col_dict)
        return response

    def read_item(self, table_name, pk_name, pk_value):
        table = self.dynamo_client.Table(table_name)
        response = table.get_item(Key={pk_name: pk_value})
        return response

    def test_db(self):
        return print(self.response)




if __name__ == '__main__':
    db = database()
    db.test_db()


## docker run -d -p 8000:8000 amazon/dynamodb-local
## docker run -p 8000:8000 -v my-volume:/dbstore amazon/dynamodb-local -jar DynamoDBLocal.jar -sharedDb -dbPath /dbstore
