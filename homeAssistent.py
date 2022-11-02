import pika
import sys
import os
import threading
'''docker run --rm -p 5672:5672 -p 8080:15672 rabbitmq:3-management'''


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
    except:

        connection.close()


def main():

    try:

        thread1 = threading.Thread(
            target=method_main, args=['measures_bright'])
        thread2 = threading.Thread(
            target=method_main,  args=['measures_temp'])
        thread3 = threading.Thread(
            target=method_main,  args=['measures_volume'])
        #thread4 = threading.Thread(ttarget=method_main,  args=['client'])

        thread1.start()
        thread2.start()
        thread3.start()
        # thread4.start()

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
