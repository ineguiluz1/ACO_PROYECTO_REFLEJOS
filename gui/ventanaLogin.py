import customtkinter as ctk
from ventanaRegister import VentanaRegister
from controller.controller import Controller
from gui import AnimatedSidebarApp

class VentanaLogin:
    def __init__(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Crear la ventana principal
        self.ventana = ctk.CTk()
        self.ventana.title("Login")
        self.ventana.geometry("1440x900+0+0")

        self.controller = Controller()

        # Evento para cerrar la ventana
        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)

        # Crear el frame principal
        self.frame = ctk.CTkFrame(self.ventana, fg_color="#2A2A2A")
        self.frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Añadir título y subtítulo
        self.titulo_subtitulo = TituloSubtitulo(self.frame, title="Bienvenido a nuestra App!!",
                                                subtitulo="Inicia sesión para jugar")

        # Agregar credenciales
        self.widget_credenciales = WidgetCredenciales(self.frame)
        self.widget_credenciales.frame.pack(pady=20)

        # Botón de inicio de sesión
        self.btn_iniciar_sesion = ctk.CTkButton(
            self.frame,
            text="Iniciar Sesión",
            font=ctk.CTkFont("Fredoka Medium", size=32),
            width=400,
            height=40,
            corner_radius=40,
            fg_color="#27AE60",
            text_color="#FFFFFF"
        )
        self.btn_iniciar_sesion.pack(pady=(0, 20))

        self.btn_iniciar_sesion.configure(command=self.inicar_sesion)

        # Crear panel de registro
        self.panel_registro = PanelRegistro(self.frame)
        self.panel_registro.frame.pack(pady=20)

        self.btn_crear_cuenta = ctk.CTkButton(
            self.frame,
            text="Crear Cuenta",
            font=ctk.CTkFont("Fredoka Medium", size=16),
            width=200,
            height=50,
            corner_radius=40,
            fg_color="#9B59B6",
            text_color="#FFFFFF"
        )
        self.btn_crear_cuenta.pack(pady=(0, 20))

        # Event handlers para cambiar color al pasar el ratón por encima
        self.btn_crear_cuenta.bind("<Enter>", self.cambiar_color_entrada)
        self.btn_crear_cuenta.bind("<Leave>", self.cambiar_color_salida)
        self.btn_crear_cuenta.configure(command=self.abrir_ventana_registro)

        # Ejecutar la ventana principal
        self.ventana.mainloop()


    # Event handlers
    def cambiar_color_entrada(self, event):
        self.btn_crear_cuenta.configure(fg_color="#8E44AD")

    def cambiar_color_salida(self, event):
        self.btn_crear_cuenta.configure(fg_color="#9B59B6")

    def abrir_ventana_registro(self):
        self.cerrar_ventana()
        VentanaRegister()

    def cerrar_ventana(self):
        self.ventana.quit()
        self.ventana.destroy()

    def inicar_sesion(self):
        email = self.widget_credenciales.entry_email.get()
        password = self.widget_credenciales.entry_contrasena.get()
        print(email, password)

        if self.controller.verificar_login(email, password, self, AnimatedSidebarApp):
            print("Inicio de sesión exitoso")
        else:
            print("Inicio de sesión fallido")



class WidgetCredenciales:
    def __init__(self, parent_frame):
        self.frame = ctk.CTkFrame(parent_frame, fg_color="#2A2A2A")
        self.frame.pack(pady=20)

        # Email input
        self.lbl_email = ctk.CTkLabel(
            self.frame, text="Email:", font=ctk.CTkFont("Fredoka Medium", size=32)
        )
        self.lbl_email.pack(pady=(10, 5))

        self.entry_email = ctk.CTkEntry(
            self.frame,
            font=ctk.CTkFont("Fredoka Medium", size=18),
            width=400,
            height=40,
            corner_radius=10,
        )
        self.entry_email.pack(pady=(0, 20))

        # Password input
        self.lbl_contrasena = ctk.CTkLabel(
            self.frame,
            text="Contraseña:",
            font=ctk.CTkFont("Fredoka Medium", size=32),
        )
        self.lbl_contrasena.pack(pady=(10, 5))

        self.entry_contrasena = ctk.CTkEntry(
            self.frame,
            font=ctk.CTkFont("Fredoka Medium", size=18),
            width=400,
            height=40,
            corner_radius=10,
            show="*",
        )
        self.entry_contrasena.pack(pady=(0, 20))


class TituloSubtitulo(ctk.CTkFrame):
    def __init__(self, parent, title, subtitulo):
        super().__init__(parent, fg_color="#2A2A2A")
        self.pack(pady=20)

        self.title_label = ctk.CTkLabel(
            self,
            text=title,
            font=ctk.CTkFont("Fredoka Medium", size=96),
            text_color="#FFFFFF",
        )
        self.title_label.pack(pady=(10, 5))

        self.subtitle_label = ctk.CTkLabel(
            self,
            text=subtitulo,
            font=ctk.CTkFont("Fredoka Medium", size=40),
            text_color="#B3B3B3",
        )
        self.subtitle_label.pack(pady=(0, 20))


class PanelRegistro:
    def __init__(self, parent_frame):
        self.frame = ctk.CTkFrame(parent_frame, fg_color="#2A2A2A")
        self.frame.pack(pady=20)

        self.lbl_no_register = ctk.CTkLabel(
            self.frame,
            text="Si no tienes cuenta puedes crear una aquí.",
            font=ctk.CTkFont("Fredoka Medium", size=20),
            text_color="#FFFFFF"
        )
        self.lbl_no_register.pack(pady=(0, 20))




if __name__ == "__main__":
    VentanaLogin()

