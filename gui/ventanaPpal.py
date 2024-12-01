import customtkinter as ctk
from PIL import Image, ImageTk

# Configuración de customtkinter
ctk.set_appearance_mode("Dark")  # Opciones: "Dark", "Light"
ctk.set_default_color_theme("blue")  # Opciones: "blue", "green", "dark-blue"

class Sidebar(ctk.CTkFrame):
    menu_color = "#383838"
    flagExpanded = False
    width_step = 10
    start_pos = 45

    def __init__(self, master, width):
        super().__init__(master, width=width, fg_color=self.menu_color)

        def extendSidebar():
            current = self.winfo_width() / 2
            print(f"Current width: {current}")
            if current < 200:  # Solo expandir si el ancho es menor que 200
                new_width = current + self.width_step
                print(f"New width: {new_width}")
                self.configure(width=new_width)
                print(f"Current width: {self.winfo_width()}")
                self.after(10, extendSidebar)

        def contractSidebar():
            current = self.winfo_width() / 2
            print(f"Current width: {current}")
            if current > 45:
                new_width = current - self.width_step
                print(f"New width: {new_width}")
                self.configure(width=new_width)
                print(f"Current width: {self.winfo_width()}")
                self.after(10, contractSidebar)

        def expandSidebar():
            if self.flagExpanded:
                # self.configure(width=45)
                contractSidebar()
                self.menuButton.updateImage("icons/menu.png")
                self.flagExpanded = False
            else:
                extendSidebar()  # Llama a extendSidebar para expandir la barra lateral
                self.menuButton.updateImage("icons/close.png")
                self.flagExpanded = True

        self.menuButton = MenuButton(self, "icons/menu.png", self.menu_color, expandSidebar, 10)
        ledButton = MenuButton(self, "icons/led.png", self.menu_color, None, 70)
        lbl_led = ctk.CTkLabel(self, text="LED Mode", fg_color=self.menu_color, font=("Arial", 20), width=100, height=30, anchor="w",padx=10)
        lbl_led.place(x=45, y=70)
        buzzerButton = MenuButton(self, "icons/buzzer.png", self.menu_color, None, 130)
        lbl_buzzer = ctk.CTkLabel(self, text="Buzzer Mode", fg_color=self.menu_color, font=("Arial", 20), width=100,
                               height=30, anchor="w", padx=10)
        lbl_buzzer.place(x=45, y=130)

        self.pack(side="left", fill="y", pady=4, padx=3)
        self.pack_propagate(False)

class MenuButton(ctk.CTkButton):
    def __init__(self, master, imagePath, color, command, y):
        icon = Image.open(imagePath).resize((50, 50))
        image = ImageTk.PhotoImage(icon)
        super().__init__(master,
                         image=image,
                         fg_color=color,
                         text="",
                         border_spacing=0,
                         width=39,
                         command=command)
        self.place(x=3, y=y)

    def updateImage(self, imagePath):
        icon = Image.open(imagePath).resize((50, 50))
        image = ImageTk.PhotoImage(icon)
        self.configure(image=image)

class AnimatedSidebarApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Medición de reflejos")
        self.geometry("800x600")

        # Crear la barra lateral
        self.sidebar = Sidebar(self, 45)

# Ejecutar la aplicación
app = AnimatedSidebarApp()
app.mainloop()