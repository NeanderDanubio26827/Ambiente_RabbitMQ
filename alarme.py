import grpc
import file_pb2_grpc as msg_pb2_grpc
import file_pb2 as msg_pb2
from concurrent import futures


class msgServiceServicer(msg_pb2_grpc.msgServiceServicer):
    def ligar(self, request, context):
        result = 'on'
        return msg_pb2.Estado(onOff=result)

    def desligar(self, request, context):
        result = 'off'
        return msg_pb2.Estado(onOff=result)


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    msg_pb2_grpc.add_msgServiceServicer_to_server(msgServiceServicer(), server)
    print('alarme online!!')
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


main()
