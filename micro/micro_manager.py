import serial
import serial
import threading
import time


class MicroManager:
    def __init__(self, port, baudrate=38400):
        self.port = port
        self.baudrate = baudrate
        self.connection = None
        self.is_connected = False  # Estado de la conexión
        self.monitor_thread = None
        self.stop_monitoring = threading.Event()

    def mode1(self):
        self.connect()
        self.send_data("1")
        self.wait_for_data()
        tiempo = self.wait_for_data()
        self.disconnect()
        return tiempo

    def mode2(self):
        self.connect()
        self.send_data("2")
        self.wait_for_data()
        tiempo = self.wait_for_data()
        self.disconnect()
        return tiempo

    def connect(self):
        try:
            self.connection = serial.Serial(self.port, baudrate=self.baudrate, timeout=1)
            self.is_connected = True
            print("Connected")
            # Iniciar el monitoreo de la conexión
            self.stop_monitoring.clear()
            self.monitor_thread = threading.Thread(target=self._monitor_connection, daemon=True)
            self.monitor_thread.start()
        except serial.SerialException as e:
            print(f"Error connecting: {e}")
            self.connection = None
            self.is_connected = False

    def send_data(self, data):
        if self.connection and self.connection.is_open:
            self.connection.write(data.encode('utf-8'))
        else:
            raise ConnectionError("Connection lost or not established.")

    def receive_data(self):
        if self.connection and self.connection.is_open:
            try:
                data = self.connection.readline().decode('utf-8').strip()
                return data
            except serial.SerialException as e:
                raise ConnectionError(f"Error reading data: {e}")
        else:
            raise ConnectionError("Connection lost or not established.")

    def disconnect(self):
        self.stop_monitoring.set()  # Detener monitoreo
        if self.connection and self.connection.is_open:
            self.connection.close()
            self.is_connected = False
            print("Connection closed.")

    def wait_for_data(self):
        if self.connection and self.connection.is_open:
            while True:
                data = self.connection.readline().decode('utf-8').strip()
                if data:
                    return data
        else:
            raise ConnectionError("Connection lost or not established.")

    def _monitor_connection(self):
        """Hilo que monitorea continuamente el estado de la conexión."""
        while not self.stop_monitoring.is_set():
            if not self.connection or not self.connection.is_open:
                self.is_connected = False
                print("Connection lost!")
                raise ConnectionError("Connection lost during monitoring.")
            time.sleep(1)  # Comprobar cada segundo


# micro.send_data("1")
# print(micro.wait_for_data())
# print(micro.wait_for_data())
# # micro.send_data("3")
# micro.disconnect()

if __name__ == '__main__':
    micro = MicroManager('COM3')
    micro.connect()
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
