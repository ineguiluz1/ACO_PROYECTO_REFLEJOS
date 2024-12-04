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
            self.connection.write(data.encode('utf-8'))

    def receive_data(self):
        data = None
        if self.connection and self.connection.is_open:
            data = self.connection.readline().decode('utf-8').strip()
        return data

    def disconnect(self):
        if self.connection and self.connection.is_open:
            self.connection.close()
            print("Conexión terminada.")

    def wait_for_data(self):
        if self.connection and self.connection.is_open:
            while True:
                data = self.connection.readline().decode('utf-8').strip()
                if data:
                    return data



micro = MicroManager('COM3')
micro.connect()
# micro.send_data("1")
# print(micro.wait_for_data())
# print(micro.wait_for_data())
# # micro.send_data("3")
# micro.disconnect()

try:
    while True:
        user_input = input("Enter command ('exit' to quit): ")
        if user_input.lower() == 'exit':
            micro.disconnect()
            break
        else:
            micro.send_data(str(user_input))
            print(f"Sent: {user_input}")
            print(micro.wait_for_data())
            print(micro.wait_for_data())
except KeyboardInterrupt:
    print("\nInterrupción detectada. Cerrando conexión.")
    micro.disconnect()
