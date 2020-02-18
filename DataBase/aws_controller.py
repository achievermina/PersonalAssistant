import boto3

class database:
    def __init__(self):
        dynamo_client = boto3.client('dynamodb', endpoint_url='http://localhost:8000/')
        response = dynamo_client.list_tables()

    def test_db(self):
        return self.response




if __name__ == '__main__':
    print("Hi")


## docker run -d -p 8000:8000 amazon/dynamodb-local