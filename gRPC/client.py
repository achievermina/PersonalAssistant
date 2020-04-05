import grpc

import indeedclone_pb2
import indeedclone_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = indeedclone_pb2_grpc.jobServiceStub(channel)

# create a valid request message
number = indeedclone_pb2_grpc.Number(value=16)

# make the call
response = stub.SquareRoot(number)

# et voilà
print(response.value)