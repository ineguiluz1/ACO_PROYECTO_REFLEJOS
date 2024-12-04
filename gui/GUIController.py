import db.db as db
from gui import AnimatedSidebarApp

class GUIController:
    def __init__(self):
        self.db = db.DB()

    def verificar_login(self, email, password, ventana_login):
        player = self.db.login_player(email, password)
        if player:
            ventana_login.ventana.destroy()
            app = AnimatedSidebarApp()
            app.mainloop()
            return True
        return False

    def registrar_jugador(self, email, password, username):
        self.db.register_player(email, password, username)