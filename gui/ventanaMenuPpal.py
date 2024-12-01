import tkinter as tk
from tkinter import ttk, font

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("App Reflejos")
ventana.geometry("1440x900")
ventana.configure(bg="#2A2A2A")  # Fondo de la ventana

# Crear un Frame para contener los widgets
frame = tk.Frame(ventana, bg="#2A2A2A")  # Fondo del Frame
frame.pack(fill="both", expand=True)

# Titulo de la ventana (APP REFLEJOS)
lbl_titulo = tk.Label(frame, text="App Reflejos", font=("Fredoka Medium", 96), bg="#2A2A2A", fg="#ffffff")
lbl_titulo.pack(pady=(80, 10))

# Subtitulo de la ventana (MIDE TUS REFLEJOS...)
lbl_subtitulo = tk.Label(frame, text="Mide tus reflejos en distintos\nmodos de juego!!", font=("Fredoka Medium", 40), bg="#2A2A2A", fg="#b3b3b3")
lbl_subtitulo.pack(pady=(0, 100))

# Boton para jugar
btn_jugar = tk.Button(frame, text="Jugar", font=("Fredoka Medium", 30), bg="#007bff", fg="#ffffff", width=27, height=2)
btn_jugar.pack(pady=(0, 20))

# Boton para salir
btn_salir = tk.Button(frame, text="Salir", font=("Fredoka Medium", 24), bg="#E74C3C", fg="#ffffff", width=25, height=2)
btn_salir.pack(pady=(0, 30))

#ventana.protocol("WM_DELETE_WINDOW", ventana.quit)


# Ejecutar el bucle principal
#ventana.mainloop()
