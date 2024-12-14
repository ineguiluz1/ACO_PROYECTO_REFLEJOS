import customtkinter as ctk
from PIL import Image, ImageTk
from customtkinter import CTkImage
from controller.controller import Controller

# controller = Controller()

# Configuración de customtkinter
ctk.set_appearance_mode("Dark")  # Opciones: "Dark", "Light"
ctk.set_default_color_theme("blue")  # Opciones: "blue", "green", "dark-blue"

class Sidebar(ctk.CTkFrame):
    menu_color = "#383838"
    flagExpanded = False
    width_step = 10

    def __init__(self, master, width):
        # super().__init__(master, width=width,fg_color=self.menu_color)
        #
        # self.master = master
        #
        # self.menuButton = MenuButton(self, "icons/menu.png", self.menu_color, self.expandSidebar, 10)
        #
        # ledButton = MenuButton(self, "icons/led.png", self.menu_color, lambda: self.switch_page("led"), 70)
        # self.led_btn_indicator = ctk.CTkLabel(self, width=3, height=30,text="", fg_color=self.menu_color)
        # self.led_btn_indicator.place(x=3, y=70)
        #
        # lbl_led = ctk.CTkLabel(self, text="LED Mode", fg_color=self.menu_color, font=("Arial", 20),
        #                        width=100, height=30, anchor="w", padx=10)
        # lbl_led.place(x=45, y=70)
        # # lbl_led.bind('<Button-1>', lambda e: self.master.show_page("led"))
        # lbl_led.bind('<Button-1>', lambda e: self.switch_page("led"))
        #
        # buzzerButton = MenuButton(self, "icons/buzzer.png", self.menu_color, lambda: self.switch_page("buzzer"), 130)
        # self.buzzer_btn_indicator = ctk.CTkLabel(self, width=3, height=30, text="", fg_color=self.menu_color)
        # self.buzzer_btn_indicator.place(x=3, y=130)
        # lbl_buzzer = ctk.CTkLabel(self, text="Buzzer Mode", fg_color=self.menu_color, font=("Arial", 20),
        #                           width=100, height=30, anchor="w", padx=10)
        # lbl_buzzer.place(x=45, y=130)
        # # lbl_buzzer.bind('<Button-1>', lambda e: self.master.show_page("buzzer"))
        # lbl_buzzer.bind('<Button-1>', lambda e: self.switch_page("buzzer"))
        #
        # self.pack(side="left", fill="y", pady=4, padx=3)
        # self.pack_propagate(False)

        super().__init__(master, width=width, fg_color=self.menu_color)

        self.master = master

        # Botón del menú
        self.menuButton = MenuButton(self, "icons/menu.png", self.menu_color, self.expandSidebar, 10)

        # LED Mode
        self.led_btn, self.led_btn_indicator, self.lbl_led = self.create_menu_item(
            image_path="icons/led.png",
            label_text="LED Mode",
            y_position=70,
            page_name="led"
        )

        # Buzzer Mode
        self.buzzer_btn, self.buzzer_btn_indicator, self.lbl_buzzer = self.create_menu_item(
            image_path="icons/buzzer.png",
            label_text="Buzzer Mode",
            y_position=130,
            page_name="buzzer"
        )

        #Leaderboard
        self.leaderboard_btn, self.leaderboard_btn_indicator, self.lbl_leaderboard = self.create_menu_item(
            image_path="icons/leaderboard.png",
            label_text="Leaderboard",
            y_position=190,
            page_name="leaderboard"
        )

        self.pack(side="left", fill="y", pady=4, padx=3)
        self.pack_propagate(False)

    def switch_page(self, page):
        """Switches the page and updates button indicators."""
        if page == "led":
            self.led_btn_indicator.configure(fg_color="#ffffff")
            self.buzzer_btn_indicator.configure(fg_color=self.menu_color)
            self.leaderboard_btn_indicator.configure(fg_color=self.menu_color)
            self.master.show_page("led")
            if self.flagExpanded:
                self.expandSidebar()

        elif page == "buzzer":
            self.led_btn_indicator.configure(fg_color=self.menu_color)
            self.buzzer_btn_indicator.configure(fg_color="#ffffff")
            self.leaderboard_btn_indicator.configure(fg_color=self.menu_color)
            self.master.show_page("buzzer")
            if self.flagExpanded:
                self.expandSidebar()

        elif page == "leaderboard":
            self.led_btn_indicator.configure(fg_color=self.menu_color)
            self.buzzer_btn_indicator.configure(fg_color=self.menu_color)
            self.leaderboard_btn_indicator.configure(fg_color="#ffffff")
            self.master.show_page("leaderboard")
            if self.flagExpanded:
                self.expandSidebar()

    def extendSidebar(self):
        current = self.winfo_width()/2
        if current < 200:
            new_width = current + self.width_step
            self.configure(width=new_width)
            self.after(10, self.extendSidebar)

    def contractSidebar(self):
        current = self.winfo_width()/2
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

    def create_menu_item(self, image_path, label_text, y_position, page_name):
        """
        Creates a menu item with an icon, a label, and an indicator.
        :param image_path: Path to the icon image.
        :param label_text: Text for the menu label.
        :param y_position: Vertical position of the menu item.
        :param page_name: Page to switch to when the item is clicked.
        """
        button = MenuButton(self, image_path, self.menu_color, lambda: self.switch_page(page_name), y_position)
        indicator = ctk.CTkLabel(self, width=3, height=30, text="", fg_color=self.menu_color)
        indicator.place(x=3, y=y_position)

        label = ctk.CTkLabel(
            self,
            text=label_text,
            fg_color=self.menu_color,
            font=("Arial", 20),
            width=100,
            height=30,
            anchor="w",
            padx=10
        )
        label.place(x=45, y=y_position)
        label.bind('<Button-1>', lambda e: self.switch_page(page_name))

        return button, indicator, label


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
        icon = Image.open(imagePath).resize((30, 30))
        self.image = CTkImage(icon, size=(30, 30))
        self.configure(image=self.image)


class LedModePage(ctk.CTkFrame):
    def __init__(self, master, controller):
        self.controller = controller
        super().__init__(master)
        self.btn_instrucciones = ctk.CTkButton(self,
                                               text="Instrucciones",
                                               font=("Fredoka Medium", 20),
                                               width=50, height=40,
                                               fg_color="#27AE60",
                                               text_color="white",
                                               corner_radius=30,
                                               command=self.show_dialog)
        self.btn_instrucciones.place(x=10, y=20)
        self.lbl_titulo = ctk.CTkLabel(self, text="LED Mode", text_color="white", font=("Fredoka Medium", 96))
        self.lbl_titulo.pack(pady=(70,20))
        self.lbl_contador = ctk.CTkLabel(self, text="0", text_color="white", font=("Fredoka Medium", 96))
        self.lbl_contador.pack(pady=(20,30))
        self.btn_retry = ctk.CTkButton(self, text="GO!", font=("Fredoka Medium", 48), width=260, height=110, fg_color="#1E90FF", text_color="white",corner_radius=25)
        self.btn_retry.pack(pady=50)
        self.btn_retry.bind("<Button-1>", lambda e: self.controller.led_button_click(self))

    def update_timer(self, tiempo):
        self.lbl_contador.configure(text=tiempo)

    def show_dialog(self):
        # Crear una ventana emergente (JOptionPane)
        dialog = ctk.CTkToplevel(self)
        dialog.title("Instrucciones")
        # dialog.geometry("300x200")
        dialog.resizable(False, False)

        # Obtener dimensiones y posición de la ventana principal
        parent_x = self.winfo_rootx()
        parent_y = self.winfo_rooty()
        parent_width = self.winfo_width()
        parent_height = self.winfo_height()

        # Calcular posición para centrar el diálogo
        dialog_width = 300
        dialog_height = 200
        pos_x = parent_x + (parent_width // 2) - (dialog_width // 2)-150
        pos_y = parent_y + (parent_height // 2) - (dialog_height // 2)-100

        dialog.geometry(f"{dialog_width}x{dialog_height}+{pos_x}+{pos_y}")

        # Hacer que la ventana aparezca sobre la principal
        dialog.transient(self.master)  # Vincula la ventana emergente a la principal
        dialog.grab_set()  # Bloquea la interacción con la ventana principal
        dialog.focus()  # Da foco a la ventana emergente

        # Etiqueta con mensaje
        label = ctk.CTkLabel(dialog,
                             text="Cuando se pulse el botón GO!, "
                                          "después de un tiempo de espera "
                                          "aleatorio se encenderá uno de "
                                          "los dos LEDs y lo tendrás que "
                                          "pulsar lo más rápido posible.",
                             font=("Arial", 16),
                             wraplength=280)
        label.pack(pady=20)

        # Botones para interactuar con el JOptionPane
        button_ok = ctk.CTkButton(dialog, text="OK", command=dialog.destroy)  # Cerrar el diálogo
        button_ok.pack(pady=10)

    def lanzarError(self,codigo):
        # Crear una ventana emergente (JOptionPane)
        dialog = ctk.CTkToplevel(self)
        dialog.title("Alerta!")
        dialog.resizable(False, False)

        # Obtener dimensiones y posición de la ventana principal
        parent_x = self.winfo_rootx()
        parent_y = self.winfo_rooty()
        parent_width = self.winfo_width()
        parent_height = self.winfo_height()

        # Calcular posición para centrar el diálogo
        dialog_width = 300
        dialog_height = 200
        pos_x = parent_x + (parent_width // 2) - (dialog_width // 2) - 150
        pos_y = parent_y + (parent_height // 2) - (dialog_height // 2) - 100

        dialog.geometry(f"{dialog_width}x{dialog_height}+{pos_x}+{pos_y}")

        # Hacer que la ventana aparezca sobre la principal
        dialog.transient(self.master)  # Vincula la ventana emergente a la principal
        dialog.grab_set()  # Bloquea la interacción con la ventana principal
        dialog.focus()  # Da foco a la ventana emergente

        if codigo == -1:
            # Etiqueta con mensaje
            label = ctk.CTkLabel(dialog,
                                 text="Error: Has pulsado el pulsador antes de tiempo.",
                                 font=("Arial", 16),
                                 wraplength=280)
            label.pack(pady=20)
        elif codigo == -2:
            # Etiqueta con mensaje
            label = ctk.CTkLabel(dialog,
                                 text="Error: Has pulsado el pulsador incorrecto.",
                                 font=("Arial", 16),
                                 wraplength=280)
            label.pack(pady=20)


        # Botones para interactuar con el JOptionPane
        button_ok = ctk.CTkButton(dialog, text="OK", command=dialog.destroy)  # Cerrar el diálogo
        button_ok.pack(pady=10)

class BuzzerModePage(ctk.CTkFrame):
    def __init__(self, master,controller):
        super().__init__(master)
        self.controller = controller
        self.btn_instrucciones = ctk.CTkButton(self,
                                               text="Instrucciones",
                                               font=("Fredoka Medium", 20),
                                               width=50, height=40, fg_color="#27AE60", text_color="white",
                                               corner_radius=30,
                                               command=self.show_dialog)
        self.btn_instrucciones.place(x=10, y=20)
        self.lbl_titulo = ctk.CTkLabel(self, text="Buzzer Mode", text_color="white", font=("Fredoka Medium", 96))
        self.lbl_titulo.pack(pady=(70,20))
        self.lbl_contador = ctk.CTkLabel(self, text="0", text_color="white", font=("Fredoka Medium", 96))
        self.lbl_contador.pack(pady=(20,30))
        self.btn_retry = ctk.CTkButton(self, text="GO!", font=("Fredoka Medium", 48), width=260, height=110, fg_color="#1E90FF", text_color="white", corner_radius=25)
        self.btn_retry.pack(pady=50)
        self.btn_retry.bind("<Button-1>", lambda e: controller.buzzer_button_click(self))

    def update_timer(self, tiempo):
        self.lbl_contador.configure(text=tiempo)

    def show_dialog(self):
        # Crear una ventana emergente (JOptionPane)
        dialog = ctk.CTkToplevel(self)
        dialog.title("Instrucciones")
        # dialog.geometry("300x200")
        dialog.resizable(False, False)

        # Obtener dimensiones y posición de la ventana principal
        parent_x = self.winfo_rootx()
        parent_y = self.winfo_rooty()
        parent_width = self.winfo_width()
        parent_height = self.winfo_height()

        # Calcular posición para centrar el diálogo
        dialog_width = 300
        dialog_height = 200
        pos_x = parent_x + (parent_width // 2) - (dialog_width // 2)-150
        pos_y = parent_y + (parent_height // 2) - (dialog_height // 2)-100

        dialog.geometry(f"{dialog_width}x{dialog_height}+{pos_x}+{pos_y}")

        # Hacer que la ventana aparezca sobre la principal
        dialog.transient(self.master)  # Vincula la ventana emergente a la principal
        dialog.grab_set()  # Bloquea la interacción con la ventana principal
        dialog.focus()  # Da foco a la ventana emergente

        # Etiqueta con mensaje
        label = ctk.CTkLabel(dialog,
                             text="Cuando se pulse el botón GO!, "
                                  "se encenderá un LED y después de "
                                  "un tiempo aleatorio sonará un pitido. "
                                  "Deberás pulsar el botón lo más rápido "
                                  "posible, después de escuchar el pitido.",
                             font=("Arial", 16),
                             wraplength=280)
        label.pack(pady=20)

        # Botones para interactuar con el JOptionPane
        button_ok = ctk.CTkButton(dialog, text="OK", command=dialog.destroy)  # Cerrar el diálogo
        button_ok.pack(pady=10)

    def lanzarError(self,codigo):
        # Crear una ventana emergente (JOptionPane)
        dialog = ctk.CTkToplevel(self)
        dialog.title("Alerta!")
        dialog.resizable(False, False)

        # Obtener dimensiones y posición de la ventana principal
        parent_x = self.winfo_rootx()
        parent_y = self.winfo_rooty()
        parent_width = self.winfo_width()
        parent_height = self.winfo_height()

        # Calcular posición para centrar el diálogo
        dialog_width = 300
        dialog_height = 200
        pos_x = parent_x + (parent_width // 2) - (dialog_width // 2) - 150
        pos_y = parent_y + (parent_height // 2) - (dialog_height // 2) - 100

        dialog.geometry(f"{dialog_width}x{dialog_height}+{pos_x}+{pos_y}")

        # Hacer que la ventana aparezca sobre la principal
        dialog.transient(self.master)  # Vincula la ventana emergente a la principal
        dialog.grab_set()  # Bloquea la interacción con la ventana principal
        dialog.focus()  # Da foco a la ventana emergente

        if codigo == -1:
            # Etiqueta con mensaje
            label = ctk.CTkLabel(dialog,
                                 text="Error: Has pulsado el pulsador antes de tiempo.",
                                 font=("Arial", 16),
                                 wraplength=280)
            label.pack(pady=20)
        elif codigo == -3:
            # Etiqueta con mensaje
            label = ctk.CTkLabel(dialog,
                                 text="Error: Has pulsado el pulsador incorrecto. Recuerda que debes pulsar al pulsador iluminado.",
                                 font=("Arial", 16),
                                 wraplength=280)
            label.pack(pady=20)


        # Botones para interactuar con el JOptionPane
        button_ok = ctk.CTkButton(dialog, text="OK", command=dialog.destroy)  # Cerrar el diálogo
        button_ok.pack(pady=10)


class LeaderboardPage(ctk.CTkFrame):
    def __init__(self, master,controller):
        super().__init__(master)
        self.controller = controller
        self.lbl_titulo = ctk.CTkLabel(self, text="Leaderboard", text_color="white", font=("Fredoka Medium", 96))
        self.lbl_titulo.pack(pady=(20,20))


class AnimatedSidebarApp(ctk.CTk):
    def __init__(self,controller):
        super().__init__(fg_color="#242424")
        self.controller = controller
        self.title("Medición de reflejos")
        self.geometry("800x600+100+100")
        self.iconbitmap("icons/stopwatch.ico")
        # self.fg_color = "#ffffff"
        # Imprimar la geometria del frame principal
        print(self.winfo_geometry())
        print(self.winfo_width(), self.winfo_height())

        self.page_frame = ctk.CTkFrame(self, fg_color="#242424")
        self.page_frame.place(relwidth=1.0, relheight=1.0, x=50)
        # Páginas
        self.pages = {"led": LedModePage(self.page_frame, self.controller),
                      "buzzer": BuzzerModePage(self.page_frame, self.controller),
                      "leaderboard": LeaderboardPage(self.page_frame,self.controller)}
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
if __name__ == "__main__":
    controller = Controller()
    app = AnimatedSidebarApp(controller)
    app.mainloop()
