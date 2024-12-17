from micro.micro_manager import MicroManager
import threading
from db.db import DB
# from gui.gui import AnimatedSidebarApp
# from gui import AnimatedSidebarApp
# import gui as gui

class Controller:
    flagEjecutando = 0
    user = 1

    def __init__(self):
        # Inicializa el MicroManager con la configuración deseada
        self.micro_manager = MicroManager(port="COM3")
        self.db = DB()


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
                if tiempo in ["-1","-2","-3"]:
                    led_page.lanzarError(int(tiempo))
                else:
                    # Actualiza el contador en la página LED
                    led_page.update_timer(tiempo)
                    self.db.save_game(self.user, "led", tiempo)
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
                if tiempo in ["-1","-2","-3"]:
                    buzzer_page.lanzarError(int(tiempo))
                else:
                    # Actualiza el contador en la página Buzzer
                    buzzer_page.update_timer(tiempo)
                    self.db.save_game(self.user, "buzzer", tiempo)
            except ConnectionError as e:
                print(f"Error: {e}")
            finally:
                # Habilitar el botón nuevamente
                buzzer_page.btn_retry.configure(state="normal")
                self.flagEjecutando = 0

    def verificar_login(self, email, password, ventana_login,gui,controller):
        player = self.db.login_player(email, password)
        player_id = player[0]
        if player:
            ventana_login.ventana.destroy()
            self.user = player_id
            print("player_id:", player_id)
            # app = gui.AnimatedSidebarApp()
            app = gui(controller)
            app.mainloop()
            return True
        return False

    def registrar_jugador(self, email, password, username):
        self.db.register_player(email, password, username)


    def save_game(self, game_mode, score):
        self.db.save_game(self.user, game_mode, score)

    def get_best_games_by_gamemode(self, game_mode):
        return self.db.get_best_games_by_gamemode(game_mode)

    def get_game_info_by_gamemode(self, game_mode):
        return self.db.get_game_info_by_gamemode(game_mode, self.user)