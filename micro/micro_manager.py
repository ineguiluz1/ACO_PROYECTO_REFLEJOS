import serial

class MicroManager:
    def __init__(self, port, baudrate=38400):
        self.port = port
        self.baudrate = baudrate
        self.connection = None


    def connect(self):
        try:
            self.connection = serial.Serial(self.port, baudrate=self.baudrate)
            if self.connection is not None:
                print("Connected")
        except serial.SerialException as e:
            print(e)
            self.connection = None

    def send_data(self, data):
        if self.connection and self.connection.is_open:
            self.connection.write(data.enconde('utf-8'))

    def receive_data(self):
        data = None
        if self.connection and self.connection.is_open:
            data = self.connection.readline().decode('utf-8').strip()
        return data

    def disconnect(self):
        if self.connection and self.connection.is_open:
            self.connection.close()
            print("Conexión terminada.")
