from micro.micro_manager import MicroManager
import threading


class Controller:
    flagEjecutando = 0

    def __init__(self):
        # Inicializa el MicroManager con la configuración deseada
        self.micro_manager = MicroManager(port="COM3")

    def led_button_click(self, led_page):
        # Crear y lanzar un hilo
        threading.Thread(target=self._led_thread, args=(led_page,), daemon=True).start()

    def _led_thread(self, led_page):
        """Lógica del botón LED ejecutada en un hilo."""
        if self.flagEjecutando == 0:
            try:
                self.flagEjecutando = 1
                # Deshabilitar el botón mientras se ejecuta
                led_page.btn_retry.configure(state="disabled")
                tiempo = self.micro_manager.mode1()

                # Actualiza el contador en la página LED
                led_page.update_timer(tiempo)
            except ConnectionError as e:
                print(f"Error: {e}")
            finally:
                # Habilitar el botón nuevamente
                led_page.btn_retry.configure(state="normal")
                self.flagEjecutando = 0

    def buzzer_button_click(self, buzzer_page):
        # Crear y lanzar un hilo
        threading.Thread(target=self._buzzer_thread, args=(buzzer_page,), daemon=True).start()

    def _buzzer_thread(self, buzzer_page):
        """Lógica del botón Buzzer ejecutada en un hilo."""
        if self.flagEjecutando == 0:
            try:
                self.flagEjecutando = 1
                # Deshabilitar el botón mientras se ejecuta
                buzzer_page.btn_retry.configure(state="disabled")
                tiempo = self.micro_manager.mode2()

                # Actualiza el contador en la página Buzzer
                buzzer_page.update_timer(tiempo)
            except ConnectionError as e:
                print(f"Error: {e}")
            finally:
                # Habilitar el botón nuevamente
                buzzer_page.btn_retry.configure(state="normal")
                self.flagEjecutando = 0
