import tkinter as tk
from tkinter import ttk, font
from tkinter import Canvas
import customtkinter as ctk
import sys

# Funciones para cambiar el color del botón
def cambiar_color_entrada(event):
    btn_crear_cuenta.config(background="#2ECC71")

def cambiar_color_salida(event):
    btn_crear_cuenta.config(background="#27AE60")


# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Registro")
ventana.geometry("1440x900")
ventana.configure(bg="#2A2A2A")

frame = tk.Frame(ventana, bg="#2A2A2A")
frame.pack(fill="both", expand=True)

lbl_titulo = tk.Label(frame, text="Crea tu cuenta!!", font=("Fredoka Medium", 96), bg="#2A2A2A", fg="#5DADE2")
lbl_titulo.pack(pady=(80, 10))



# Crear los campos de entrada (Email, Contraseña y Nickname)
lbl_email = tk.Label(frame, text="Email:", font=("Fredoka Medium", 24), bg="#2A2A2A", fg="#ffffff")
lbl_email.pack(pady=(10, 5))

entry_email = tk.Entry(frame, font=("Fredoka Medium", 24), width=30, bg="#FAD7A0")
entry_email.pack(pady=(0, 20))

lbl_contrasena = tk.Label(frame, text="Contraseña:", font=("Fredoka Medium", 24), bg="#2A2A2A", fg="#ffffff")
lbl_contrasena.pack(pady=(10, 5))

entry_contrasena = tk.Entry(frame, font=("Fredoka Medium", 24), width=30, show="*", bg="#FAD7A0") # 'show' oculta la contraseña
entry_contrasena.pack(pady=(0, 20))

lbl_nickname = tk.Label(frame, text="Nickname:", font=("Fredoka Medium", 24), bg="#2A2A2A", fg="#ffffff")
lbl_nickname.pack(pady=(10, 5))

entry_nickname = tk.Entry(frame, font=("Fredoka Medium", 24), width=30, bg="#FAD7A0")
entry_nickname.pack(pady=(0, 40))

# Crear el botón "Crear Cuenta"
btn_crear_cuenta = tk.Button(frame, text="Crear Cuenta", font=("Fredoka Medium", 24), bg="#27AE60", fg="#ffffff", width=20, height=2)
btn_crear_cuenta.pack(pady=(10, 10))

# Asociar los eventos de entrada y salida del cursor con el botón
btn_crear_cuenta.bind("<Enter>", cambiar_color_entrada)
btn_crear_cuenta.bind("<Leave>", cambiar_color_salida)

# Añadir el protocolo de la ventana
ventana.protocol("WM_DELETE_WINDOW", ventana.quit)

# Iniciar el bucle principal
ventana.mainloop()