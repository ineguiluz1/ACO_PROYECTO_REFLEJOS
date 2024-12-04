from micro.micro_manager import MicroManager

class Controller:
    flagEjecutando = 0

    def __init__(self):
        # Inicializa el MicroManager con la configuración deseada
        self.micro_manager = MicroManager(port="COM3")

    def led_button_click(self, led_page):
        # Maneja eventos del botón LED
        if self.flagEjecutando == 0:
            try:
                self.flagEjecutando = 1
                tiempo = self.micro_manager.mode1()
                # print(f"LED command sent. Tiempo: {tiempo}")

                # Actualiza el contador en la página LED
                led_page.update_timer(tiempo)
                self.flagEjecutando = 0
            except ConnectionError as e:
                print(f"Error: {e}")

    def buzzer_button_click(self):
        # Maneja eventos del botón Buzzer
        try:
            self.micro_manager.connect()
            self.micro_manager.send_data("Buzz")
            print("Buzzer command sent.")
        except ConnectionError as e:
            print(f"Error: {e}")
        finally:
            self.micro_manager.disconnect()
