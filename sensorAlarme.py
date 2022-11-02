import pika
from time import sleep

'''Classe para o Alarme
ID, se necessário
status, para saber se está ligado ou não
name, nome do sensor
volume, xxxxxxxxxxx'''


class Sensor_Alarme:
    def __init__(self, ID, status, name, volume):
        self.ID = ID
        self.status = status
        self.name = name
        self.volume = volume
        self.device = 3

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

    '''def get(self):
        return self.volume'''


r1 = input("create new sensor for Alarm? \n")
Id = None
s1 = None
name = None
r2 = None
Volume = None


def fun():
    return


if r1 == 'yes':

    Id = input("What ID's sensor?\n")
    r2 = input("Is On the sensor?\n")
    name = input("What's name's sensor? \n")
    if r2 == 'ON' or r2 == 'on':
        Volume = input("What the is volume's alarm?\n")
    else:
        Volume = 'zero'

    s1 = Sensor_Alarme(Id, r2, name, Volume)

    while True:
        print("Bringing connect")
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='measures_volume')

        while True:
            try:
                sleep(5)
                msg = s1.volume
                channel.basic_publish(exchange='',
                                      routing_key='measures_volume',
                                      body=msg)
                print("A mensagem foi enviada!")

            except:
                connection.close()
else:
    fun()
