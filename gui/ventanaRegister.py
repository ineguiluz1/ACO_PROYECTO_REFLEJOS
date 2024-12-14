import customtkinter as ctk
from controller.controller import Controller


class VentanaRegister:
    def __init__(self,controller):
        # Initialize CustomTkinter (theme and scaling)
        ctk.set_appearance_mode("dark")  # Modes: "System", "Dark", "Light"
        ctk.set_default_color_theme("blue")  # Themes: "blue", "dark-blue", "green"

        # Create the main window
        self.ventana = ctk.CTk()
        self.ventana.title("Registro")
        self.ventana.geometry("800x600+0+0")

        # Create the GUI controller
        self.controller = controller

        # Create the main frame
        self.frame = ctk.CTkFrame(self.ventana, fg_color="#2A2A2A")
        self.frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Add widgets
        self.crear_widgets()

        # Bind register
        self.btn_crear_cuenta.configure(command=self.registrar_jugador)

        # Run the main loop
        self.ventana.mainloop()

    def registrar_jugador(self):
        email = self.entry_email.get()
        password = self.entry_contrasena.get()
        username = self.entry_nickname.get()
        self.controller.registrar_jugador(email, password, username)

    def crear_widgets(self):
        # Title label
        lbl_titulo = ctk.CTkLabel(
            self.frame,
            text="Crea tu cuenta!!",
            font=ctk.CTkFont("Fredoka Medium", size=72),
            text_color="#5DADE2",
        )
        lbl_titulo.pack(pady=(80, 10))

        # Email input
        lbl_email = ctk.CTkLabel(
            self.frame, text="Email:", font=ctk.CTkFont("Fredoka Medium", size=24)
        )
        lbl_email.pack(pady=(10, 5))

        self.entry_email = ctk.CTkEntry(
            self.frame,
            font=ctk.CTkFont("Fredoka Medium", size=20),
            width=400,
            height=40,
            corner_radius=10,
        )
        self.entry_email.pack(pady=(0, 10))

        # Password input
        lbl_contrasena = ctk.CTkLabel(
            self.frame,
            text="Contraseña:",
            font=ctk.CTkFont("Fredoka Medium", size=24),
        )
        lbl_contrasena.pack(pady=(5, 2))

        self.entry_contrasena = ctk.CTkEntry(
            self.frame,
            font=ctk.CTkFont("Fredoka Medium", size=20),
            width=400,
            height=40,
            corner_radius=10,
            show="*",
        )
        self.entry_contrasena.pack(pady=(0, 10))

        # Nickname input
        lbl_nickname = ctk.CTkLabel(
            self.frame, text="Nickname:", font=ctk.CTkFont("Fredoka Medium", size=24)
        )
        lbl_nickname.pack(pady=(5, 2))

        self.entry_nickname = ctk.CTkEntry(
            self.frame,
            font=ctk.CTkFont("Fredoka Medium", size=20),
            width=400,
            height=40,
            corner_radius=10,
        )
        self.entry_nickname.pack(pady=(0, 20))

        # Create account button
        self.btn_crear_cuenta = ctk.CTkButton(
            self.frame,
            text="Crear Cuenta",
            font=ctk.CTkFont("Fredoka Medium", size=24),
            width=300,
            height=50,
            corner_radius=50,
            fg_color="#27AE60",
            text_color="#ffffff"
        )
        self.btn_crear_cuenta.pack(pady=(5, 5))

        # Bind hover events to the button
        self.btn_crear_cuenta.bind("<Enter>", self.cambiar_color_entrada)
        self.btn_crear_cuenta.bind("<Leave>", self.cambiar_color_salida)

    # Event handlers
    def cambiar_color_entrada(self, event):
        self.btn_crear_cuenta.configure(fg_color="#2ECC71")

    def cambiar_color_salida(self, event):
        self.btn_crear_cuenta.configure(fg_color="#27AE60")

