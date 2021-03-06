# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from gRPC import indeedclone_pb2 as gRPC_dot_indeedclone__pb2


class jobServiceStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Search = channel.unary_unary(
                '/scrapper.jobService/Search',
                request_serializer=gRPC_dot_indeedclone__pb2.searchRequest.SerializeToString,
                response_deserializer=gRPC_dot_indeedclone__pb2.searchResponse.FromString,
                )


class jobServiceServicer(object):
    """Missing associated documentation comment in .proto file"""

    def Search(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_jobServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Search': grpc.unary_unary_rpc_method_handler(
                    servicer.Search,
                    request_deserializer=gRPC_dot_indeedclone__pb2.searchRequest.FromString,
                    response_serializer=gRPC_dot_indeedclone__pb2.searchResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'scrapper.jobService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class jobService(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def Search(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/scrapper.jobService/Search',
            gRPC_dot_indeedclone__pb2.searchRequest.SerializeToString,
            gRPC_dot_indeedclone__pb2.searchResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
