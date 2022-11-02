import pika
from time import sleep

'''Classe para o Ar-cond
ID, se necessário
status, para saber se está ligado ou não
name, nome do sensor
temp, temperatura do AR'''


class Sensor_Ar:
    def __init__(self, ID, status, name, temp):
        self.ID = ID
        self.status = status
        self.name = name
        self.temp = temp

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

    ''' def get(self):
        return self.temp'''


r1 = input("create new sensor for Air? \n")
Id = None
s1 = None
name = None
r2 = None
temp = None


def fun():
    return


if r1 == 'yes':

    Id = input("What ID's sensor?\n")
    r2 = input("Is On the sensor?\n")
    name = input("What's name's sensor? \n")
    if r2 == 'ON' or r2 == 'on':
        temp = input("What the is temp's room?\n")
    else:
        temp = 'zero'

    s1 = Sensor_Ar(Id, r2, name, temp)

    while True:
        print("Bringing connect")
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost'))
        '''faz a conexão com o RabbitMQ'''
        channel = connection.channel()
        '''Cria uma fila 'measures_temp' '''
        channel.queue_declare(queue='measures_temp')

        '''Laço para a leitura do sensor'''
        while True:
            try:
                sleep(5)
                msg = s1.temp
                channel.basic_publish(exchange='', routing_key='measures_temp',
                                      body=msg)
                print("A mensagem foi enviada!")

            except:
                connection.close()
else:
    fun()
