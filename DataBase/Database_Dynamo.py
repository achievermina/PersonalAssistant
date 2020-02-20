import boto3

class database:
    def __init__(self):
        dynamo_client = boto3.client('dynamodb', endpoint_url='http://localhost:8000/')
        self.response = dynamo_client.list_tables()

    def test_db(self):
        return print(self.response)




if __name__ == '__main__':
    db = database()
    db.test_db()


## docker run -d -p 8000:8000 amazon/dynamodb-local