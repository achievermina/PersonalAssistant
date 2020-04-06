import grpc
from gRPC import indeedclone_pb2, indeedclone_pb2_grpc

def search(searchTerm):
    print("Start service")
    try:
      channel = grpc.insecure_channel('localhost:3000')
      stub = indeedclone_pb2_grpc.jobServiceStub(channel)
      response = stub.Search(indeedclone_pb2.searchRequest(term=searchTerm))
      return response

    except Exception as e:
      print(e)
      return e


if __name__ =="__main__":
    result = search("python")
    print(result)