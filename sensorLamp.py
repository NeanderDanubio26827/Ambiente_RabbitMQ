
import pika
from time import sleep

'''Classe para a lâmpada
ID, se necessário
status, para saber se está ligado ou não
name, nome do sensor
bright, brilho da lâmpada'''


class Sensor_Lamp:
    def __init__(self, ID, status, name, bright):
        self.ID = ID
        self.status = status
        self.name = name
        self.device = 1
        self.bright = bright

    def on_sensor(self):
        if self.status == 'OFF' or self.status == 'off':
            self.status = 'ON'
        else:
            print("Device already is ON")

    def off_sensor(self):
        if self.status == 'ON' or self.status == 'on':
            self.status = 'OFF'
        else:
            print("Device already is OFF")

    def to_measure_publish(self, status):
        self.status = status

    def type_of_device(self):
        return self.device


r1 = input("create new sensor for lamp? \n")
Id = None
s1 = None
name = None
r2 = None
bright = None


def fun():
    return


if r1 == 'yes':

    Id = input("What ID's sensor?\n")
    r2 = input("Is On the sensor?\n")
    name = input("What's name's sensor? \n")
    if r2 == 'ON' or r2 == 'on':
        bright = input("What the bright's lamp?\n")
    else:
        bright = 'zero'

    s1 = Sensor_Lamp(Id, r2, name, bright)

    while True:
        print("Bringing connect")
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        channel.queue_declare(
            queue='measures_bright')

        while True:
            try:
                sleep(5)
                msg = s1.bright
                channel.basic_publish(exchange='',
                                      routing_key='measures_bright',
                                      body=msg)
                print("A mensagem foi enviada!")

            except:
                connection.close()
else:
    fun()
