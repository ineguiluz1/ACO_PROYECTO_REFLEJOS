import tkinter as tk
from tkinter import Canvas, Button, PhotoImage
from pathlib import Path


class VentanaMenu(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Selector de Modo de Juego")
        self.geometry("700x500")
        
        # Panel izquierdo
        self.frame_izquierdo = tk.Frame(self, width=150, bg="#cccccc")
        self.frame_izquierdo.pack(side="left", fill="y")

        # Centrar los botones en el panel izquierdo
        self.botones_frame = tk.Frame(self.frame_izquierdo, bg="#cccccc")
        self.botones_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Opciones de modos de juego
        self.modos = ["Reacción Visual", "Reacción Auditiva"]

        for modo in self.modos:
            btn = tk.Button(
                self.botones_frame, 
                text=modo, 
                command=lambda m=modo: self.cambiar_contenido(m)
            )
            btn.pack(pady=10, fill="x", padx=10)

        # Panel derecho (contenido dinámico)
        self.frame_derecho = tk.Frame(self, bg="#505050")
        self.frame_derecho.pack(side="right", expand=True, fill="both")

        # Mensaje inicial
        self.cambiar_contenido(None)

    def cambiar_contenido(self, modo):
        # Limpiar el contenido actual
        for widget in self.frame_derecho.winfo_children():
            widget.destroy()

        if modo == "Reacción Visual":
            self.mostrar_reaccion_visual()
        elif modo == "Reacción Auditiva":
            label = tk.Label(self.frame_derecho, text="Entrena tus reflejos auditivos reaccionando a sonidos.",
                             font=("Arial", 12), bg="#505050", fg="white")
            label.pack(pady=20)
        else:
            label = tk.Label(self.frame_derecho, text="Selecciona un modo de juego.",
                             font=("Arial", 12), bg="#505050", fg="white")
            label.pack(pady=20)

    def mostrar_reaccion_visual(self):
        # Ruta relativa a los assets
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"../frame0")

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        canvas = Canvas(
            self.frame_derecho,
            bg="#505050",
            height=500,
            width=700,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        canvas.pack(fill="both", expand=True)

        image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        canvas.create_image(
            359.0,
            250.0,
            image=image_image_1
        )

        canvas.create_text(
            195.0,
            180.0,
            anchor="nw",
            text="0.000",
            fill="#FFFFFF",
            font=("Lalezar Regular", 128 * -1)
        )

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            self.frame_derecho,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        button_1.image = button_image_1  # Evitar que la imagen sea recolectada por el garbage collector
        button_1.place(
            x=297.0,
            y=381.0,
            width=125.0,
            height=43.0
        )

        image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        canvas.create_image(
            350.0,
            34.0,
            image=image_image_2
        )


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Ocultar la ventana principal
    ventana = VentanaMenu(master=root)
    ventana.mainloop()