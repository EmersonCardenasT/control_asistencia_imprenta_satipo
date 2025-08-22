import customtkinter as ctk
import os
from PIL import Image

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sistema de Asistencia - Imprenta XYZ")
        self.geometry("900x550")

        # --------- LOGIN FRAME ---------
        self.login_frame = ctk.CTkFrame(self, corner_radius=10)
        self.login_frame.pack(expand=True)

        lbl_title = ctk.CTkLabel(self.login_frame, text="Iniciar Sesión", font=ctk.CTkFont(size=20, weight="bold"))
        lbl_title.pack(pady=(30, 10))

        self.username_entry = ctk.CTkEntry(self.login_frame, placeholder_text="Usuario")
        self.username_entry.pack(pady=10, padx=40)

        self.password_entry = ctk.CTkEntry(self.login_frame, placeholder_text="Contraseña", show="*")
        self.password_entry.pack(pady=10, padx=40)

        self.login_button = ctk.CTkButton(self.login_frame, text="Ingresar", command=self.check_login)
        self.login_button.pack(pady=20)

        self.login_msg = ctk.CTkLabel(self.login_frame, text="", text_color="red")
        self.login_msg.pack()

        # --------- MAIN APP (Oculto hasta login) ---------
        self.navigation_frame = None
        self.home_frame = None
        self.second_frame = None
        self.third_frame = None

    # --------- VALIDACIÓN LOGIN ---------
    def check_login(self):
        user = self.username_entry.get()
        password = self.password_entry.get()

        if user == "admin" and password == "1234":  # 🔑 Aquí pones tu validación real
            self.login_frame.pack_forget()  # Ocultar login
            self.create_main_app()          # Mostrar la app principal
        else:
            self.login_msg.configure(text="Usuario o contraseña incorrectos")

    def logout(self):
        # Ocultar frames principales
        if self.navigation_frame:
            self.navigation_frame.grid_forget()
        if self.home_frame:
            self.home_frame.grid_forget()
        if self.second_frame:
            self.second_frame.grid_forget()
        if self.third_frame:
            self.third_frame.grid_forget()

        # Volver a mostrar el login
        self.login_frame.pack(expand=True)

        # Limpiar campos
        self.username_entry.delete(0, "end")
        self.password_entry.delete(0, "end")
        self.login_msg.configure(text="")


    # --------- APP PRINCIPAL ---------
    def create_main_app(self):
        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # carga de imágenes
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        self.logo_image = ctk.CTkImage(Image.open(os.path.join(image_path, "CustomTkinter_logo_single.png")), size=(26, 26))
        self.large_test_image = ctk.CTkImage(Image.open(os.path.join(image_path, "large_test_image.png")), size=(500, 150))
        self.image_icon_image = ctk.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.home_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                       dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.chat_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                       dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(20, 20))
        self.add_user_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
                                           dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(20, 20))

        # create navigation frame
        self.navigation_frame = ctk.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = ctk.CTkLabel(self.navigation_frame, text="  Sistema Asistencia", image=self.logo_image,
                                                   compound="left", font=ctk.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Inicio",
                                         fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                         image=self.home_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Reportes",
                                            fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                            image=self.chat_image, anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = ctk.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Empleados",
                                            fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                            image=self.add_user_image, anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        # OptionMenu de modo oscuro
        self.appearance_mode_menu = ctk.CTkOptionMenu(
            self.navigation_frame,
            values=["Light", "Dark", "System"],
            command=self.change_appearance_mode_event
        )
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=(20, 10), sticky="s")  # 👈 ahora sí aparece

        # Botón de cerrar sesión
        self.logout_button = ctk.CTkButton(
            self.navigation_frame,
            text="Cerrar Sesión",
            fg_color="red",
            hover_color="darkred",
            text_color="white",
            corner_radius=8,
            command=self.logout
        )
        self.logout_button.grid(row=7, column=0, padx=20, pady=(0, 20), sticky="s")




        # create home frame
        self.home_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame_large_image_label = ctk.CTkLabel(self.home_frame, text="", image=self.large_test_image)
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        self.home_frame_button_1 = ctk.CTkButton(self.home_frame, text="Reconocimiento Facial", image=self.image_icon_image)
        self.home_frame_button_1.grid(row=1, column=0, padx=20, pady=10)

        # create second frame
        self.second_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        lbl2 = ctk.CTkLabel(self.second_frame, text="📊 Aquí irán los reportes", font=ctk.CTkFont(size=18))
        lbl2.pack(pady=50)

        # create third frame
        self.third_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        lbl3 = ctk.CTkLabel(self.third_frame, text="👥 Administración de empleados", font=ctk.CTkFont(size=18))
        lbl3.pack(pady=50)

        # select default frame
        self.select_frame_by_name("home")

    # --------- FRAMES NAV ---------
    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def change_appearance_mode_event(self, new_appearance_mode):
        ctk.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    ctk.set_appearance_mode("light")  # puedes poner "dark"
    ctk.set_default_color_theme("blue")  # o "green", "dark-blue"
    app = App()
    app.mainloop()
