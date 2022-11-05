'''Import necessários'''
import pika
from time import sleep
import sensorAir
import sensorAlarme
import sensorLamp
import sys
import os

'''function main'''


def main():
    r1 = input("create new sensor? \n")

    Id = input("What ID's sensor?\n")
    r1 = input("Is On the sensor?\n")
    name = input("What's name's sensor? \n")
    device = input("For what device is sensor?\n")

    if device == '1':
        s1 = sensorLamp.Sensor_Lamp(Id, r1, name, device)
        connection1 = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        channel1 = connection1.channel()
        channel1.queue_declare(queue='measures_bright')
        while True:

            sleep(5)
            msg = s1.get()
            channel1.basic_publish(exchange='',
                                   routing_key='measures_bright',
                                   body=msg)
            print("The message was sent!")

    if device == '2':

        s2 = sensorAir.Sensor_Ar(Id, r1, name, device)
        connection2 = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        channel2 = connection2.channel()
        channel2.queue_declare(queue='measures_temp')
        while True:

            sleep(5)
            msg = s2.get()
            channel2.basic_publish(exchange='',
                                   routing_key='measures_temp',
                                   body=msg)
            print("The message was sent!")

    if device == '3':
        s3 = sensorAlarme.Sensor_Alarme(Id, r1, name, device)
        connection3 = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        channel3 = connection3.channel()
        channel3.queue_declare(queue='measures_alarme')
        while True:

            sleep(5)
            msg = s3.get
            channel3.basic_publish(exchange='',
                                   routing_key='measures_alarme',
                                   body=msg)
            print("The message was sent!")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
