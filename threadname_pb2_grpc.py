# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import threadname_pb2 as threadname__pb2


class ThreadNamerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetThreadName = channel.unary_unary(
                '/ThreadNamer/GetThreadName',
                request_serializer=threadname__pb2.ThreadNameRequest.SerializeToString,
                response_deserializer=threadname__pb2.ThreadNameResponse.FromString,
                )


class ThreadNamerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetThreadName(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ThreadNamerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetThreadName': grpc.unary_unary_rpc_method_handler(
                    servicer.GetThreadName,
                    request_deserializer=threadname__pb2.ThreadNameRequest.FromString,
                    response_serializer=threadname__pb2.ThreadNameResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ThreadNamer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ThreadNamer(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetThreadName(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ThreadNamer/GetThreadName',
            threadname__pb2.ThreadNameRequest.SerializeToString,
            threadname__pb2.ThreadNameResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)