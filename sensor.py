

class Sensor:
    def __init__(self, ID, status, name, device):
        self.ID = ID
        self.status = status
        self.name = name
        self.device = device

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
