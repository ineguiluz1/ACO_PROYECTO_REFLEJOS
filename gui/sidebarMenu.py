import customtkinter as ctk
from PIL import Image, ImageTk
from customtkinter import CTkImage

from controller.controller import Controller

# Configuración de customtkinter
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class Sidebar(ctk.CTkFrame):
    menu_color = "#383838"
    flagExpanded = False
    width_step = 10

    def __init__(self, master, width):
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
            # self.master.get_page("leaderboard").refresh_data()
            self.master.get_page("leaderboard").update_labels()
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
        # dialog.after(200, lambda: dialog.iconbitmap('icons/stopwatch.ico'))
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
    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        # Title
        title_label = ctk.CTkLabel(self, text="Leaderboard", text_color="white", font=("Fredoka Medium", 86))
        title_label.pack(pady=(20, 10))

        # Frame for the two panels
        panel_frame = ctk.CTkFrame(self)
        panel_frame.pack(fill="both", expand=True)

        # Initialize data for both tables (empty initially)
        self.led_data = controller.get_best_games_by_gamemode("led")
        self.buzzer_data = controller.get_best_games_by_gamemode("buzzer")

        # Stats for LED mode
        self.game_info_led = controller.get_game_info_by_gamemode("led")

        #Stats for Buzzer mode
        self.game_info_buzzer = controller.get_game_info_by_gamemode("buzzer")

        # To store references to labels
        self.led_labels = []
        self.buzzer_labels = []

        # Panel 1 (Blue)
        self.panelStatsLeds(panel_frame)

        # Panel 2 (Red)
        self.panelStatsBuzzer(panel_frame)



    def panelStatsLeds(self, panel_frame):
        # Panel 1 (Led)
        panel = ctk.CTkFrame(panel_frame, fg_color="gray17", border_color="white")
        panel.place(relx=0, rely=0, relwidth=0.47, relheight=1)

        # Title
        title_label = ctk.CTkLabel(panel, text="Led Mode", text_color="white", font=("Fredoka Medium", 24))
        title_label.pack(pady=(20, 10))

        # Create the enumeration table
        self.create_enumeration_with_attributes(panel, self.led_data, self.led_labels)

        # Create game stats for LED
        self.create_game_stats_led(panel, self.game_info_led)



    def panelStatsBuzzer(self, panel_frame):
        # Panel 2 (Buzzer)
        panel = ctk.CTkFrame(panel_frame, fg_color="gray17", border_color="white")
        panel.place(relx=0.47, rely=0, relwidth=0.47, relheight=1)

        title_label = ctk.CTkLabel(panel, text="Buzzer Mode", text_color="white", font=("Fredoka Medium", 24))
        title_label.pack(pady=(20, 10))

        # Create the enumeration table
        self.create_enumeration_with_attributes(panel, self.buzzer_data, self.buzzer_labels)

        # Create game stats for buzzer
        self.create_game_stats_buzzer(panel, self.game_info_buzzer)

    def create_enumeration_with_attributes(self, parent, data, label_storage):
        # Frame to hold the table
        frame = ctk.CTkFrame(parent)
        frame.pack(fill="both", expand=True, padx=10, pady=(0,5))

        # Table headers
        headers = ["Pos", "Nombre", "Valor"]

        for col_num, header in enumerate(headers):
            header_label = ctk.CTkLabel(frame, text=header, width=20, anchor="w")
            header_label.grid(row=0, column=col_num, padx=0, pady=5)

        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=2)
        frame.grid_columnconfigure(2, weight=1)

        # Create rows for the data
        for row_num, (id_, name, value) in enumerate(data, start=1):
            row_color = "gray17" if row_num % 2 == 0 else "gray25"
            row_frame = ctk.CTkFrame(frame, fg_color=row_color)
            row_frame.grid(row=row_num, column=0, columnspan=3, sticky="ew", padx=10, pady=5)

            # Define and store labels for later updates
            id_label = ctk.CTkLabel(row_frame, text=str(id_), width=10)
            name_label = ctk.CTkLabel(row_frame, text=name, width=120)
            value_label = ctk.CTkLabel(row_frame, text=str(value), width=10)

            id_label.grid(row=0, column=0, padx=10, pady=5)
            name_label.grid(row=0, column=1, padx=10, pady=5)
            value_label.grid(row=0, column=2, padx=10, pady=5)

            row_frame.grid_columnconfigure(0, weight=1)
            row_frame.grid_columnconfigure(1, weight=2)
            row_frame.grid_columnconfigure(2, weight=1)

            # Save label references
            label_storage.append((id_label, name_label, value_label))

    def create_game_stats_led(self, parent, data):
        # Create a frame for the statistics
        frame = ctk.CTkFrame(parent, fg_color="transparent")
        frame.pack(fill="x", padx=10, pady=20)

        # Create and store references to labels
        self.led_stats_labels = {}

        self.led_stats_labels['n_games'] = ctk.CTkLabel(frame, text="Número de juegos: " + str(data[0][0]),
                                                        text_color="white", font=("Fredoka Medium", 14))
        self.led_stats_labels['n_games'].pack(anchor="w", padx=10, pady=2)

        self.led_stats_labels['avg_score'] = ctk.CTkLabel(frame, text="Puntuación media: " + str(data[0][1]),
                                                          text_color="white", font=("Fredoka Medium", 14))
        self.led_stats_labels['avg_score'].pack(anchor="w", padx=10, pady=2)

        self.led_stats_labels['best_score'] = ctk.CTkLabel(frame, text="Mejor puntuación: " + str(data[0][2]),
                                                           text_color="white", font=("Fredoka Medium", 14))
        self.led_stats_labels['best_score'].pack(anchor="w", padx=10, pady=2)

    def create_game_stats_buzzer(self, parent, data):
        # Create a frame for the statistics
        frame = ctk.CTkFrame(parent, fg_color="transparent")
        frame.pack(fill="x", padx=10, pady=20)

        # Create and store references to labels
        self.buzzer_stats_labels = {}

        self.buzzer_stats_labels['n_games'] = ctk.CTkLabel(frame, text="Número de juegos: " + str(data[0][0]),
                                                           text_color="white", font=("Fredoka Medium", 14))
        self.buzzer_stats_labels['n_games'].pack(anchor="w", padx=10, pady=2)

        self.buzzer_stats_labels['avg_score'] = ctk.CTkLabel(frame, text="Puntuación media: " + str(data[0][1]),
                                                             text_color="white", font=("Fredoka Medium", 14))
        self.buzzer_stats_labels['avg_score'].pack(anchor="w", padx=10, pady=2)

        self.buzzer_stats_labels['best_score'] = ctk.CTkLabel(frame, text="Mejor puntuación: " + str(data[0][2]),
                                                              text_color="white", font=("Fredoka Medium", 14))
        self.buzzer_stats_labels['best_score'].pack(anchor="w", padx=10, pady=2)

    def update_labels(self):
        # Update LED data
        self.led_data = self.controller.get_best_games_by_gamemode("led")
        for i, (id_label, name_label, value_label) in enumerate(self.led_labels):
            id_, name, value = self.led_data[i]
            # id_label.configure(text=str(id_))
            name_label.configure(text=name)
            value_label.configure(text=str(value))

        # Update buzzer data
        self.buzzer_data = self.controller.get_best_games_by_gamemode("buzzer")
        for i, (id_label, name_label, value_label) in enumerate(self.buzzer_labels):
            id_, name, value = self.buzzer_data[i]
            name_label.configure(text=name)
            value_label.configure(text=str(value))

        self.game_info_led = self.controller.get_game_info_by_gamemode("led")
        self.game_info_buzzer = self.controller.get_game_info_by_gamemode("buzzer")

        self.led_stats_labels['n_games'].configure(text="Número de juegos: " + str(self.game_info_led[0][0]))
        self.led_stats_labels['avg_score'].configure(text="Puntuación media: " + str(self.game_info_led[0][1]))
        self.led_stats_labels['best_score'].configure(text="Mejor puntuación: " + str(self.game_info_led[0][2]))

        self.buzzer_stats_labels['n_games'].configure(text="Número de juegos: " + str(self.game_info_buzzer[0][0]))
        self.buzzer_stats_labels['avg_score'].configure(text="Puntuación media: " + str(self.game_info_buzzer[0][1]))
        self.buzzer_stats_labels['best_score'].configure(text="Mejor puntuación: " + str(self.game_info_buzzer[0][2]))

class AnimatedSidebarApp(ctk.CTk):
    def __init__(self,controller):
        super().__init__(fg_color="#242424")
        self.controller = controller
        self.title("Medición de reflejos")
        self.geometry("800x600+100+100")
        self.iconbitmap("icons/stopwatch.ico")
        self.resizable(False, False)

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

    def get_page(self, page_name):
        return self.pages[page_name]


# Ejecutar la aplicación
if __name__ == "__main__":
    controller = Controller()
    app = AnimatedSidebarApp(controller)
    app.mainloop()
