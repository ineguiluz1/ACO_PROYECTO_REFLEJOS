import tkinter as tk
from tkinter import messagebox
from ttkbootstrap import Window, Label, Frame, Entry, Button
'''
def register():
    username = entry_username.get()
    email = entry_email.get()
    password = entry_password.get()
    confirm_password = entry_confirm_password.get()
    
    if not username or not email or not password or not confirm_password:
        messagebox.showerror("Error", "Todos los campos son obligatorios.")
        return
    
    if password != confirm_password:
        messagebox.showerror("Error", "Las contraseñas no coinciden.")
        return
    
    # Lógica para manejar el registro aquí
    messagebox.showinfo("Registro exitoso", "¡Te has registrado con éxito!")
    root.destroy()  # Cierra la ventana después de registrar.

# Configurar ventana principal
root = ttk.Window(themename="darkly")  # Cambia el tema si prefieres
root.title("Registro")
root.geometry("1000x800")  # Ventana más grande
root.resizable(False, False)

# Título
title_label = ttk.Label(root, text="Registro de Jugador", font=("Helvetica", 26, "bold"))
title_label.pack(pady=40)

# Campo de formulario
frame_form = ttk.Frame(root, padding=30)
frame_form.pack(pady=20)

# Nombre de Usuario
label_username = ttk.Label(frame_form, text="Nombre de Usuario", font=("Helvetica", 14))
label_username.grid(row=0, column=0, pady=10, sticky="w")
entry_username = ttk.Entry(frame_form, font=("Helvetica", 14), width=30)
entry_username.grid(row=0, column=1, pady=10, padx=20)

# Correo Electrónico
label_email = ttk.Label(frame_form, text="Correo Electrónico", font=("Helvetica", 14))
label_email.grid(row=1, column=0, pady=10, sticky="w")
entry_email = ttk.Entry(frame_form, font=("Helvetica", 14), width=30)
entry_email.grid(row=1, column=1, pady=10, padx=20)

# Contraseña
label_password = ttk.Label(frame_form, text="Contraseña", font=("Helvetica", 14))
label_password.grid(row=2, column=0, pady=10, sticky="w")
entry_password = ttk.Entry(frame_form, show="*", font=("Helvetica", 14), width=30)
entry_password.grid(row=2, column=1, pady=10, padx=20)

# Confirmar Contraseña
label_confirm_password = ttk.Label(frame_form, text="Confirmar Contraseña", font=("Helvetica", 14))
label_confirm_password.grid(row=3, column=0, pady=10, sticky="w")
entry_confirm_password = ttk.Entry(frame_form, show="*", font=("Helvetica", 14), width=30)
entry_confirm_password.grid(row=3, column=1, pady=10, padx=20)

# Botón de registro
button_register = ttk.Button(root, text="Registrarse", command=register, bootstyle="success")
button_register.pack(pady=40, ipadx=30, ipady=10)

# Pie de página
footer_label = ttk.Label(root, text="© 2024 Tu Juego. Todos los derechos reservados.", font=("Helvetica", 12))
footer_label.pack(side="bottom", pady=20)

root.mainloop()

'''
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

