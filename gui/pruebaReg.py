import tkinter as tk
from tkinter import messagebox

class VentanaRegistro:
    def __init__(self, master=None, usuarios=None):
        self.ventana = tk.Toplevel(master) if master else tk.Tk()
        self.ventana.title("Registro")
        self.ventana.geometry("1440x900")
        self.ventana.configure(bg="#2A2A2A")

        self.usuarios = usuarios 
        frame = tk.Frame(self.ventana, bg="#2A2A2A")
        frame.pack(fill="both", expand=True)

        lbl_titulo = tk.Label(frame, text="Crea tu cuenta!!", font=("Fredoka Medium", 96), bg="#2A2A2A", fg="#5DADE2")
        lbl_titulo.pack(pady=(80, 10))
        lbl_email = tk.Label(frame, text="Email:", font=("Fredoka Medium", 24), bg="#2A2A2A", fg="#ffffff")
        lbl_email.pack(pady=(10, 5))

        self.entry_email = tk.Entry(frame, font=("Fredoka Medium", 24), width=30, bg="#FAD7A0")
        self.entry_email.pack(pady=(0, 20))

        lbl_contrasena = tk.Label(frame, text="Contraseña:", font=("Fredoka Medium", 24), bg="#2A2A2A", fg="#ffffff")
        lbl_contrasena.pack(pady=(10, 5))

        self.entry_contrasena = tk.Entry(frame, font=("Fredoka Medium", 24), width=30, show="*", bg="#FAD7A0")  # 'show' oculta la contraseña
        self.entry_contrasena.pack(pady=(0, 20))

        lbl_nickname = tk.Label(frame, text="Nickname:", font=("Fredoka Medium", 24), bg="#2A2A2A", fg="#ffffff")
        lbl_nickname.pack(pady=(10, 5))

        self.entry_nickname = tk.Entry(frame, font=("Fredoka Medium", 24), width=30, bg="#FAD7A0")
        self.entry_nickname.pack(pady=(0, 40))

        self.btn_crear_cuenta = tk.Button(frame, text="Crear Cuenta", font=("Fredoka Medium", 24), bg="#27AE60", fg="#ffffff", width=20, height=2)
        self.btn_crear_cuenta.pack(pady=(10, 10))

        self.btn_crear_cuenta.config(command=self.guardar_usuario)

        self.ventana.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)

        self.ventana.mainloop()

    def cambiar_color_entrada(self, event):
        self.btn_crear_cuenta.config(background="#2ECC71")

    def cambiar_color_salida(self, event):
        self.btn_crear_cuenta.config(background="#27AE60")

    def guardar_usuario(self):
        email = self.entry_email.get()
        contrasena = self.entry_contrasena.get()
        nickname = self.entry_nickname.get()

        if email and contrasena and nickname:
            if email not in self.usuarios:
                self.usuarios[email] = contrasena 
                print(f"Usuario registrado: {email}, Contraseña: {contrasena}")
                
                self.ventana.destroy()
                messagebox.showinfo("Error en el inicio de sesión","Usuario registrado correctamente")
            else:
                messagebox.showinfo("Error", "El correo electrónico ya está registrado.")
        else:
            messagebox.showinfo("Error", "Por favor, complete todos los campos.")

    def cerrar_ventana(self):
        self.ventana.destroy()



