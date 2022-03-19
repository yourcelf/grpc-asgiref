import threading

import grpc.aio
from asgiref.sync import async_to_sync, sync_to_async

from threadname_pb2 import ThreadNameRequest, ThreadNameResponse
from threadname_pb2_grpc import (
    ThreadNamerServicer,
    ThreadNamerStub,
    add_ThreadNamerServicer_to_server,
)


@sync_to_async
def sync_to_async_thread_name():
    return threading.current_thread().name


class Servicer(ThreadNamerServicer):
    async def GetThreadName(self, request, context=None):
        name = await sync_to_async_thread_name()
        return ThreadNameResponse(name=name)


class Server:
    def __init__(self, addr):
        self.addr = addr

    async def __aenter__(self):
        self.server = grpc.aio.server()
        self.server.add_insecure_port(self.addr)
        add_ThreadNamerServicer_to_server(Servicer, self.server)
        await self.server.start()
        return self

    async def __aexit__(self, *args, **kwargs):
        await self.server.stop(0)


@async_to_sync
async def make_request(unused_tcp_port):
    addr = f"localhost:{unused_tcp_port}"
    server = Server(addr)
    channel = grpc.aio.insecure_channel(addr)

    async with server:
        async with channel:
            stub = ThreadNamerStub(channel)
            return await stub.GetThreadName(ThreadNameRequest())


def test_grpc_sync_to_async_thread_name(unused_tcp_port):
    cur_thread_name = threading.current_thread().name
    cur_sync_to_async_thread_name = async_to_sync(sync_to_async_thread_name)()
    assert cur_thread_name == cur_sync_to_async_thread_name

    grpc_sync_to_async_thread_name = make_request(unused_tcp_port).name
    assert grpc_sync_to_async_thread_name == cur_thread_name
