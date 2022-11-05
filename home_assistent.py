import grpc
import atuador_pb2
import atuador_pb2_grpc

def run(): 
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = atuador_pb2_grpc.msgServiceStub(channel)
        lampada = stub.ligar(atuador_pb2.Vazio())
        print(lampada)
    
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = atuador_pb2_grpc.msgServiceStub(channel)
        alarme = stub.desligar(atuador_pb2.Vazio())
        print(alarme)

    with grpc.insecure_channel('localhost:50050') as channel:
        stub = atuador_pb2_grpc.msgServiceStub(channel)
        ar = stub.ligar(atuador_pb2.Vazio())
        print(ar)

if __name__ == '__main__':
    run() 