import customtkinter as ctk
from PIL import Image, ImageTk
from customtkinter import CTkImage


# Configuración de customtkinter
ctk.set_appearance_mode("Dark")  # Opciones: "Dark", "Light"
ctk.set_default_color_theme("blue")  # Opciones: "blue", "green", "dark-blue"


class Sidebar(ctk.CTkFrame):
    menu_color = "#383838"
    flagExpanded = False
    width_step = 10

    def __init__(self, master, width):
        super().__init__(master, width=width,fg_color=self.menu_color)
        self.master = master

        self.menuButton = MenuButton(self, "icons/menu.png", self.menu_color, self.expandSidebar, 10)

        ledButton = MenuButton(self, "icons/led.png", self.menu_color, lambda: self.switch_page("led"), 70)
        self.led_btn_indicator = ctk.CTkLabel(self, width=3, height=30,text="", fg_color=self.menu_color)
        self.led_btn_indicator.place(x=3, y=70)

        lbl_led = ctk.CTkLabel(self, text="LED Mode", fg_color=self.menu_color, font=("Arial", 20),
                               width=100, height=30, anchor="w", padx=10)
        lbl_led.place(x=45, y=70)
        # lbl_led.bind('<Button-1>', lambda e: self.master.show_page("led"))
        lbl_led.bind('<Button-1>', lambda e: self.switch_page("led"))

        buzzerButton = MenuButton(self, "icons/buzzer.png", self.menu_color, lambda: self.switch_page("buzzer"), 130)
        self.buzzer_btn_indicator = ctk.CTkLabel(self, width=3, height=30, text="", fg_color=self.menu_color)
        self.buzzer_btn_indicator.place(x=3, y=130)
        lbl_buzzer = ctk.CTkLabel(self, text="Buzzer Mode", fg_color=self.menu_color, font=("Arial", 20),
                                  width=100, height=30, anchor="w", padx=10)
        lbl_buzzer.place(x=45, y=130)
        # lbl_buzzer.bind('<Button-1>', lambda e: self.master.show_page("buzzer"))
        lbl_buzzer.bind('<Button-1>', lambda e: self.switch_page("buzzer"))

        self.pack(side="left", fill="y", pady=4, padx=3)
        self.pack_propagate(False)

    def switch_page(self, page):
        """Switches the page and updates button indicators."""
        if page == "led":
            self.led_btn_indicator.configure(fg_color="#ffffff")
            self.buzzer_btn_indicator.configure(fg_color=self.menu_color)
            self.master.show_page("led")
            if self.flagExpanded:
                self.expandSidebar()

        elif page == "buzzer":
            self.led_btn_indicator.configure(fg_color=self.menu_color)
            self.buzzer_btn_indicator.configure(fg_color="#ffffff")
            self.master.show_page("buzzer")
            if self.flagExpanded:
                self.expandSidebar()

    def extendSidebar(self):
        current = self.winfo_width()
        if current < 200:
            new_width = current + self.width_step
            self.configure(width=new_width)
            self.after(10, self.extendSidebar)

    def contractSidebar(self):
        current = self.winfo_width()
        # print(f"Current width: {current}")
        if current > 45:
            self.configure(width=45)
            # new_width = current - 10
            # self.configure(width=new_width)
            # self.after(10, contractSidebar)

    def expandSidebar(self):
        if self.flagExpanded:
            self.contractSidebar()
            self.menuButton.updateImage("icons/menu.png")
            self.flagExpanded = False
        else:
            self.extendSidebar()
            self.menuButton.updateImage("icons/close.png")
            self.flagExpanded = True



class MenuButton(ctk.CTkButton):
    def __init__(self, master, imagePath, color, command, y):
        # icon = Image.open(imagePath).resize((50, 50))
        icon = Image.open(imagePath).resize((30, 30))
        self.image = CTkImage(icon,size=(30,30))
        super().__init__(master,
                         image=self.image,
                         fg_color=color,
                         text="",
                         border_spacing=0,
                         width=39,
                         command=command)
        self.place(x=3, y=y)

    def updateImage(self, imagePath):
        icon = Image.open(imagePath).resize((50, 50))
        self.image = ImageTk.PhotoImage(icon)
        self.configure(image=self.image)


class LedModePage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)  # Cambiado 'bg' por 'fg_color'
        self.lbl_titulo = ctk.CTkLabel(self, text="LED Mode", text_color="white", font=("Fredoka Medium", 96))
        self.lbl_titulo.pack(pady=10)
        self.lbl_contador = ctk.CTkLabel(self, text="00:00", text_color="white", font=("Fredoka Medium", 96))
        self.lbl_contador.pack(pady=50)
        self.btn_retry = ctk.CTkButton(self, text="Retry", font=("Fredoka Medium", 48), width=260, height=110, fg_color="#1E90FF", text_color="white")
        self.btn_retry.pack(pady=70)




class BuzzerModePage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="#32a852")  # Cambiado 'bg' por 'fg_color'
        lbl = ctk.CTkLabel(self, text="Buzzer Mode", fg_color="#2A2A2A", text_color="white", font=("Fredoka Medium", 96))
        lbl.pack(pady=10)



class AnimatedSidebarApp(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color="#242424")
        self.title("Medición de reflejos")
        self.geometry("800x600")
        self.iconbitmap("icons/stopwatch.ico")
        # self.fg_color = "#ffffff"

        self.page_frame = ctk.CTkFrame(self, fg_color="#242424")
        self.page_frame.place(relwidth=1.0, relheight=1.0, x=50)
        # Páginas
        self.pages = {}
        self.pages["led"] = LedModePage(self.page_frame)
        self.pages["buzzer"] = BuzzerModePage(self.page_frame)


        self.sidebar = Sidebar(self, 45)


        # Mostrar la página inicial
        self.show_page("led")
        self.current_page = "led"
        self.sidebar.switch_page(self.current_page)

    def show_page(self, page_name):
        for page in self.pages.values():
            page.pack_forget()
        self.pages[page_name].pack(fill="both", expand=True, pady=4, padx=3)




# Ejecutar la aplicación
app = AnimatedSidebarApp()
app.mainloop()
