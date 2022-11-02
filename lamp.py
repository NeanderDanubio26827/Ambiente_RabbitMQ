import operate as operate


class Lamp(operate.Operate):
    def __init__(self, status, ID, name, type, bright):
        self.bright = bright
        super().__init__(status, ID, name, type)

    def on_lamp(self):
        if self.status == 'OFF' or self.status == 'off':
            self.status = 'ON'
        else:
            print("Device already is ON")

    def off_lamp(self):
        if self.status == 'ON' or self.status == 'on':
            self.status = 'OFF'
        else:
            print("Device already is OFF")

    def adjust_brightness(self, value):
        self.bright = value

    def get_bright(self):
        return self.bright
