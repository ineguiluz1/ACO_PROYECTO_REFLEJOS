import tkinter as tk
from tkinter import messagebox
from ttkbootstrap import Window, Label, Frame, Entry, Button
from tkinter import Toplevel, messagebox



class VentanaRegistro:
    def __init__(self, master):
        self.master = master
        self.window = Toplevel(master)
        self.window.title("Registro")
        self.window.geometry("800x500")
        self.window.resizable(False, False)

        self._crear_componentes()

    def _crear_componentes(self):
        title_label = Label(self.window, text="Registro de Jugador", font=("Helvetica", 26, "bold"))
        title_label.pack(pady=40)

        frame_form = Frame(self.window, padding=30)
        frame_form.pack(pady=20)

        Label(frame_form, text="Nombre de Usuario", font=("Helvetica", 14)).grid(row=0, column=0, pady=10, sticky="w")
        self.entry_username = Entry(frame_form, font=("Helvetica", 14), width=30)
        self.entry_username.grid(row=0, column=1, pady=10, padx=20)

        Label(frame_form, text="Correo Electrónico", font=("Helvetica", 14)).grid(row=1, column=0, pady=10, sticky="w")
        self.entry_email = Entry(frame_form, font=("Helvetica", 14), width=30)
        self.entry_email.grid(row=1, column=1, pady=10, padx=20)

        Label(frame_form, text="Contraseña", font=("Helvetica", 14)).grid(row=2, column=0, pady=10, sticky="w")
        self.entry_password = Entry(frame_form, show="*", font=("Helvetica", 14), width=30)
        self.entry_password.grid(row=2, column=1, pady=10, padx=20)

        Label(frame_form, text="Confirmar Contraseña", font=("Helvetica", 14)).grid(row=3, column=0, pady=10, sticky="w")
        self.entry_confirm_password = Entry(frame_form, show="*", font=("Helvetica", 14), width=30)
        self.entry_confirm_password.grid(row=3, column=1, pady=10, padx=20)

        button_register = Button(self.window, text="Registrarse", command=self.register, bootstyle="success")
        button_register.pack(pady=40, ipadx=30, ipady=10)

    def register(self):
        """Lógica para manejar el registro del usuario"""
        username = self.entry_username.get()
        email = self.entry_email.get()
        password = self.entry_password.get()
        confirm_password = self.entry_confirm_password.get()

        if not username or not email or not password or not confirm_password:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")
            return

        if password != confirm_password:
            messagebox.showerror("Error", "Las contraseñas no coinciden.")
            return

        messagebox.showinfo("Registro exitoso", "¡Te has registrado con éxito!")
        self.window.destroy()

