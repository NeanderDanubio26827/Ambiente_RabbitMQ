import grpc
import pika
import sys
import os
import threading
import file_pb2_grpc
import file_pb2
'''docker run --rm -p 5672:5672 -p 8080:15672 rabbitmq:3-management'''

last_read_lamp = None
last_read_Air = None
last_read_Alarm = None
last_read_sensor_lamp = None
last_read_sensor_Air = None
last_read_sensor_Alarm = None


def fun():
    return


def method_main(arg):
    try:
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        channel.queue_declare(queue=arg)

        def callback(ch, method, properties, body):
            print(" [x] Received %r" % body)

        channel.basic_consume(
            queue=arg, on_message_callback=callback, auto_ack=True)

        print(' [*] Waiting for messages. To exit press CTRL+C')
        channel.start_consuming()
    except print():

        connection.close()


"""Método para fazer os sensores lerem"""


def method_for_grpc1():

    try:
        print("Bringing connect")
        with grpc.insecure_channel('localhost:50051') as channel1:
            stub = file_pb2_grpc.msgServiceStub(channel1)
            lampada = stub.ligar(file_pb2.Vazio())
            print(lampada)
    except print(0):
        pass


def method_for_grpc2():
    try:
        print("Bringing connect")
        with grpc.insecure_channel('localhost:50052') as channel2:
            stub = file_pb2_grpc.msgServiceStub(channel2)
            alarme = stub.desligar(file_pb2.Vazio())
            print(alarme)
    except print(0):
        pass


def method_for_grpc3():
    try:
        print("Bringing connect")
        with grpc.insecure_channel('localhost:50053') as channel3:
            stub = file_pb2_grpc.msgServiceStub(channel3)
            ar = stub.ligar(file_pb2.Vazio())
            print(ar)
    except print(0):
        pass


def main():

    try:

        thread1 = threading.Thread(
            target=method_main, args=['measures_bright'])
        thread2 = threading.Thread(
            target=method_main,  args=['measures_temp'])
        thread3 = threading.Thread(
            target=method_main,  args=['measures_volume'])
        thread4 = threading.Thread(
            target=method_for_grpc1, args=[])
        thread5 = threading.Thread(
            target=method_for_grpc2, args=[])
        thread6 = threading.Thread(
            target=method_for_grpc3,  args=[])

        thread1.start()
        thread2.start()
        thread3.start()
        thread4.start()
        thread5.start()
        thread6.start()

    except print(0):
        fun()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
