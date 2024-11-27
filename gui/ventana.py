from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox
from PIL import Image, ImageTk
from ventanaMenu import VentanaMenu
from Pruebas import VentanaRegistro

class VentanaPrincipal:
    def __init__(self):
        """Usuario de ejemplo"""
        self.usuario = "ejemplo@gmail.com"
        self.contraseña = "1234"

        """Path de las imágenes"""
        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path(r"C:\Users\mpsua\OneDrive\Escritorio\ud\TERCERO\ACO\proyecto\ventana\build\assets\frame0")

        self.window = Tk()
        self.window.geometry("1024x768")
        self.window.configure(bg="#FFFFFF")
        self.window.title("Login")
        self.window.resizable(False, False)

        self.canvas = Canvas(
            self.window,
            bg="#FFFFFF",
            height=768,
            width=1200,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)

        bg_image_path = self.relative_to_assets("image_1.png")
        original_image = Image.open(bg_image_path) 
        resized_image = original_image.resize((1024,768), Image.Resampling.LANCZOS) 
        self.bg_image = ImageTk.PhotoImage(resized_image)  

        self.canvas.create_image(0, 0, image=self.bg_image, anchor="nw")
        self._crear_componentes()
        self.window.mainloop()

    def relative_to_assets(self, path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    def _crear_componentes(self):
        entry_image_1 = PhotoImage(file=self.relative_to_assets("entry_1.png"))
        self.canvas.create_image(111.0, 366.0, image=entry_image_1)
        self.entryPwd = Entry(
            self.window,
            show="*",
            bd=0,
            bg="#9CC1D8",
            fg="#000716",
            highlightthickness=0
        )
        self.entryPwd.place(x=16.0, y=650.0, width=190.0, height=18.0)

        entry_image_2 = PhotoImage(file=self.relative_to_assets("entry_2.png"))
        self.canvas.create_image(111.0, 308.0, image=entry_image_2)
        self.entryEmail = Entry(
            self.window,
            bd=0,
            bg="#9CC1D8",
            fg="#000716",
            highlightthickness=0
        )
        self.entryEmail.place(x=16.0, y=600.0, width=190.0, height=18.0)

        """TEXTOS DE EMAIL Y CONTRASEÑA"""
        self.canvas.create_text(
            16.0,
            630.0,
            anchor="nw",
            text="Contraseña:",
            fill="#FEFEFE",
            font=("Inter", 12 * -1)
        )
        self.canvas.create_text(
            16.0,
            580.0,
            anchor="nw",
            text="Email:",
            fill="#FFFFFF",
            font=("Inter", 12 * -1)
        )

        loginButton = Button(
            self.window,
            text="Iniciar Sesion",
            command=self.login,
            bg="#4CAF50",
            fg="#FFFFFF",
            relief="flat",
            font=("Inter", 12, "bold")
        )
        loginButton.place(x=20.0, y=680.0, width=180.0, height=25.0)

        registerButton = Button(
            self.window,
            text="Registrarse",
            command=self.register,
            bg="#4CAF50",
            fg="#FFFFFF",
            relief="flat",
            font=("Inter", 12, "bold")
        )
        registerButton.place(x=20.0, y=715.0, width=180.0, height=25.0)

    def login(self):
        email = self.entryEmail.get()
        password = self.entryPwd.get()
        if email == self.usuario and password == self.contraseña:
            self.window.withdraw()
            VentanaMenu(master=self.window)
        else:
            messagebox.showinfo("Error en el inicio de sesión", "Usuario o contraseña incorrectos")

    def register(self):
        VentanaRegistro(master=self.window)


if __name__ == "__main__":
    VentanaPrincipal()
