import customtkinter as ctk
import os
from PIL import Image
import tkinter.messagebox as mbox  # al inicio del archivo
from database.connection import create_connection
from utils.empleados_utils import obtener_empleados
from utils.empleados_table import render_tabla_empleados

# Crear conexión
conn = create_connection()

def configurar_combobox_cargo(combobox):
    conexion = create_connection()
    if conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT id, nombre FROM cargo")
        resultados = cursor.fetchall()
        conexion.close()

        # Guardamos {nombre: id} para poder recuperarlo luego
        cargos_dict = {fila[1]: fila[0] for fila in resultados}

        # Asignar nombres al combobox
        combobox.configure(values=list(cargos_dict.keys()))
        if cargos_dict:
            combobox.set(list(cargos_dict.keys())[0])  # Seleccionar el primero
        return cargos_dict  # lo devolvemos para usarlo más tarde
    return {}

# Ejemplo: ejecutar un query
# if conn:
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM empleados")
#     resultados = cursor.fetchall()
#     for fila in resultados:
#         print(fila)
#     cursor.close()
#     conn.close()


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sistema de Asistencia - Imprenta XYZ")
        # --- Centrar ventana ---
        ancho_ventana = 1150
        alto_ventana = 700
        x_ventana = int((self.winfo_screenwidth() / 2) - (ancho_ventana / 2))
        y_ventana = int((self.winfo_screenheight() / 2) - (alto_ventana / 2))
        self.geometry(f"{ancho_ventana}x{alto_ventana}+{x_ventana}+{y_ventana}")


        # --------- LOGIN FRAME ---------
        self.login_frame = ctk.CTkFrame(self, corner_radius=10)
        self.login_frame.pack(expand=True)

        lbl_title = ctk.CTkLabel(
            self.login_frame,
            text="Iniciar Sesión",
            font=ctk.CTkFont(size=20, weight="bold")
        )
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
        self.navbar_frame = None
        self.home_frame = None
        self.second_frame = None
        self.third_frame = None

        self.logged_user = None  # Guardar el usuario logueado

    # --------- VALIDACIÓN LOGIN ---------
    def check_login(self):
        user = self.username_entry.get()
        password = self.password_entry.get()

        if user == "admin" and password == "1234":  # 🔑 Aquí pones tu validación real
            self.logged_user = user
            self.login_frame.pack_forget()  # Ocultar login
            self.create_main_app()          # Mostrar la app principal
        else:
            self.login_msg.configure(text="Usuario o contraseña incorrectos")

    def logout(self):
        # Ocultar frames principales
        if self.navigation_frame:
            self.navigation_frame.grid_forget()
        if self.navbar_frame:
            self.navbar_frame.grid_forget()
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
        # set grid layout 2x2 → navbar arriba, sidebar a la izquierda
        self.grid_rowconfigure(1, weight=1)  # contenido principal
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
        self.user_icon = ctk.CTkImage(Image.open(os.path.join(image_path, "add_user_dark.png")), size=(20, 20))
        # Cargar el icono de apagar
        self.logout_icon = ctk.CTkImage(
            Image.open(os.path.join(image_path, "encendido.png")), 
            size=(23, 23)
        )
        # --------- NAVBAR SUPERIOR ---------
        self.navbar_frame = ctk.CTkFrame(self, height=50, corner_radius=0)
        self.navbar_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.navbar_frame.grid_columnconfigure(0, weight=1)  # espacio flexible a la izquierda

        # Selector de modo claro/oscuro
        self.appearance_mode_menu = ctk.CTkOptionMenu(
            self.navbar_frame,
            values=["Light", "Dark", "System"],
            command=self.change_appearance_mode_event
        )
        self.appearance_mode_menu.grid(row=0, column=1, padx=10, pady=10, sticky="e")

        # Usuario logueado
        self.user_label = ctk.CTkLabel(
            self.navbar_frame,
            text=f"{self.logged_user}",
            image=self.user_icon,
            compound="left",
            font=ctk.CTkFont(size=13, weight="bold")
        )
        self.user_label.grid(row=0, column=2, padx=10, pady=10, sticky="e")

        # Botón con el icono y el comando correcto
        self.logout_button = ctk.CTkButton(
            self.navbar_frame,
            text="",
            image=self.logout_icon,
            width=40,
            fg_color="transparent",
            hover_color="darkred",
            text_color="white",
            corner_radius=8,
            command=self.confirm_logout   # 👈 aquí va la función de confirmar logout
        )

        self.logout_button.grid(row=0, column=3, padx=20, pady=10, sticky="e")

        # --------- SIDEBAR (ASIDE) ---------
        self.navigation_frame = ctk.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=1, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(5, weight=1)

        self.navigation_frame_label = ctk.CTkLabel(
            self.navigation_frame,
            text="  Sistema Asistencia",
            image=self.logo_image,
            compound="left",
            font=ctk.CTkFont(size=15, weight="bold")
        )
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = ctk.CTkButton(
            self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Inicio",
            fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
            image=self.home_image, anchor="w", command=self.home_button_event
        )
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = ctk.CTkButton(
            self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Registrar Empleado",
            fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
            image=self.add_user_image, anchor="w", command=self.frame_2_button_event
        )
        self.frame_2_button.grid(row=2, column=0, sticky="ew")

        self.frame_3_button = ctk.CTkButton(
            self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Empleados",
            fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
            image=self.add_user_image, anchor="w", command=self.frame_3_button_event
        )
        self.frame_3_button.grid(row=3, column=0, sticky="ew")

        # --------- FRAMES DE CONTENIDO ---------
        self.home_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

         # --------- DASHBOARD WIDGETS ---------
        dashboard_frame = ctk.CTkFrame(self.home_frame, fg_color="#f5f5f5", corner_radius=12)
        dashboard_frame.grid(row=0, column=0, padx=40, pady=(30, 10), sticky="ew")
        dashboard_frame.grid_columnconfigure((0,1,2,3), weight=1)

        # Widget: Empleados registrados
        widget_emp = ctk.CTkFrame(dashboard_frame, fg_color="#1976d2", corner_radius=10)
        widget_emp.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        ctk.CTkLabel(widget_emp, text="👥", font=ctk.CTkFont(size=32), text_color="#fff").pack(pady=(10,0))
        ctk.CTkLabel(widget_emp, text="Empleados", font=ctk.CTkFont(size=14, weight="bold"), text_color="#fff").pack()
        ctk.CTkLabel(widget_emp, text="25", font=ctk.CTkFont(size=22, weight="bold"), text_color="#fff").pack(pady=(0,10))

        # Widget: Asistencias registradas
        widget_asist = ctk.CTkFrame(dashboard_frame, fg_color="#388e3c", corner_radius=10)
        widget_asist.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        ctk.CTkLabel(widget_asist, text="✅", font=ctk.CTkFont(size=32), text_color="#fff").pack(pady=(10,0))
        ctk.CTkLabel(widget_asist, text="Asistencias", font=ctk.CTkFont(size=14, weight="bold"), text_color="#fff").pack()
        ctk.CTkLabel(widget_asist, text="120", font=ctk.CTkFont(size=22, weight="bold"), text_color="#fff").pack(pady=(0,10))

        # Widget: Tardanzas
        widget_tarde = ctk.CTkFrame(dashboard_frame, fg_color="#fbc02d", corner_radius=10)
        widget_tarde.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")
        ctk.CTkLabel(widget_tarde, text="⏰", font=ctk.CTkFont(size=32), text_color="#fff").pack(pady=(10,0))
        ctk.CTkLabel(widget_tarde, text="Tardanzas", font=ctk.CTkFont(size=14, weight="bold"), text_color="#fff").pack()
        ctk.CTkLabel(widget_tarde, text="8", font=ctk.CTkFont(size=22, weight="bold"), text_color="#fff").pack(pady=(0,10))

        # Widget: Faltas
        widget_falta = ctk.CTkFrame(dashboard_frame, fg_color="#d32f2f", corner_radius=10)
        widget_falta.grid(row=0, column=3, padx=10, pady=10, sticky="nsew")
        ctk.CTkLabel(widget_falta, text="❌", font=ctk.CTkFont(size=32), text_color="#fff").pack(pady=(10,0))
        ctk.CTkLabel(widget_falta, text="Faltas", font=ctk.CTkFont(size=14, weight="bold"), text_color="#fff").pack()
        ctk.CTkLabel(widget_falta, text="3", font=ctk.CTkFont(size=22, weight="bold"), text_color="#fff").pack(pady=(0,10))

        # Imagen decorativa debajo del dashboard
        self.home_frame_large_image_label = ctk.CTkLabel(self.home_frame, text="", image=self.large_test_image)
        self.home_frame_large_image_label.grid(row=1, column=0, padx=20, pady=10)

        # self.home_frame_button_1 = ctk.CTkButton(self.home_frame, text="Reconocimiento Facial", image=self.image_icon_image)
        # self.home_frame_button_1.grid(row=2, column=0, padx=20, pady=10)

        # self.home_frame_large_image_label = ctk.CTkLabel(self.home_frame, text="", image=self.large_test_image)
        # self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        # self.home_frame_button_1 = ctk.CTkButton(self.home_frame, text="Reconocimiento Facial", image=self.image_icon_image)
        # self.home_frame_button_1.grid(row=1, column=0, padx=20, pady=10)

        # --------- FRAME REGISTRAR EMPLEADO ---------
        self.second_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.second_frame.grid_columnconfigure(0, weight=1)
        
        lbl2 = ctk.CTkLabel(self.second_frame, text="📝 Registrar Empleado", font=ctk.CTkFont(size=18, weight="bold"))
        lbl2.pack(pady=20)

        # Formulario de registro estilo DNI
        form_frame = ctk.CTkFrame(self.second_frame, fg_color="#f5f5f5", corner_radius=12)
        form_frame.pack(padx=40, pady=10, fill="x")

        campos = [
            ("Nombre(s)", "nombre"),
            ("Apellido(s)", "apellido"),
            ("DNI", "dni"),
            ("Teléfono", "telefono"),
            # Los siguientes tres irán juntos en una sola fila
            ("Género", "genero"),
            ("Fecha de Nacimiento", "fecha_nacimiento"),
            ("Cargo", "cargo_id"),
            ("Dirección", "direccion"),
            ("Email", "email"),
        ]
        self.registro_vars = {}

        # Inputs de 2 en 2, excepto la fila especial de 3 campos
        i = 0
        while i < len(campos):
            # Si estamos en la fila de género, fecha_nacimiento y cargo
            if campos[i][1] == "genero":
                row_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
                row_frame.pack(fill="x", padx=10)
                for j in range(3):
                    label, key = campos[i + j]
                    col_frame = ctk.CTkFrame(row_frame, fg_color="transparent")
                    col_frame.pack(side="left", expand=True, fill="x", padx=5)
                    lbl = ctk.CTkLabel(col_frame, text=label, anchor="w")
                    lbl.pack(pady=(10,0), fill="x")

                    if key == "cargo_id":  # 👈 aquí hacemos el cambio
                        entry = ctk.CTkComboBox(col_frame)
                        cargos_dict = configurar_combobox_cargo(entry)  # llenar desde la BD
                        self.cargos_dict = cargos_dict  # guardamos el dict para consultar luego
                    elif key == "genero":
                        entry = ctk.CTkComboBox(col_frame, values=["Masculino", "Femenino", "Otro"])
                    else:
                        entry = ctk.CTkEntry(col_frame, placeholder_text=label)

                    entry.pack(pady=(0,5), fill="x")
                    self.registro_vars[key] = entry
                i += 3
            else:
                row_frame = ctk.CTkFrame(form_frame, fg_color="transparent")
                row_frame.pack(fill="x", padx=10)
                for j in range(2):
                    if i + j < len(campos) and campos[i + j][1] != "genero":
                        label, key = campos[i + j]
                        col_frame = ctk.CTkFrame(row_frame, fg_color="transparent")
                        col_frame.pack(side="left", expand=True, fill="x", padx=5)
                        lbl = ctk.CTkLabel(col_frame, text=label, anchor="w")
                        lbl.pack(pady=(10,0), fill="x")
                        entry = ctk.CTkEntry(col_frame, placeholder_text=label)
                        entry.pack(pady=(0,5), fill="x")
                        self.registro_vars[key] = entry
                i += 2

        # Botón de Registro Facial
        btn_facial = ctk.CTkButton(
            form_frame,
            text="" \
            " Facial",
            fg_color="#1976d2",
            hover_color="#1565c0",
            text_color="white",
            corner_radius=8,
            command=self.registro_facial_event
        )
        btn_facial.pack(pady=30)
        # FIN DE FRAME REGISTRO A EMPLEADO

        # --------- EMPLEADOS FRAME ---------
        self.third_frame = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.third_frame.grid_columnconfigure(0, weight=1)

        lbl3 = ctk.CTkLabel(self.third_frame, text="👥 Administración de empleados", font=ctk.CTkFont(size=18))
        lbl3.pack(pady=20)

        # Botón para abrir formulario de registro
        btn_add_employee = ctk.CTkButton(
            self.third_frame,
            text="➕ Registrar Empleado",
            fg_color="green",
            hover_color="darkgreen",
            text_color="white",
            command=self.open_register_employee_window
        )
        btn_add_employee.pack(pady=10)
 
        # --------- BUSCADOR ---------
        self.search_var = ctk.StringVar()
        search_entry = ctk.CTkEntry(self.third_frame, textvariable=self.search_var, placeholder_text="Buscar empleado...")
        search_entry.pack(pady=10)

        btn_search = ctk.CTkButton(self.third_frame, text="🔍 Buscar", width=100, command=lambda: self.cargar_tabla_empleados(1))
        btn_search.pack(pady=5)

        # --------- TABLA ---------
        self.table_frame = ctk.CTkFrame(self.third_frame)
        self.table_frame.pack(pady=10, padx=40, fill="x")  # <<--- padding lateral


        # --------- PAGINACIÓN ---------
        self.pagination_frame = ctk.CTkFrame(self.third_frame, fg_color="transparent")
        self.pagination_frame.pack(pady=10)

        self.pagina_actual = 1
        self.cargar_tabla_empleados(1)

        # FIN DEL FRAME DE EMPLEADOS

        # select default frame
        self.select_frame_by_name("home")

    # --------- FRAMES NAV ---------
    def select_frame_by_name(self, name):
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

        if name == "home":
            self.home_frame.grid(row=1, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=1, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=1, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

    def open_register_employee_window(self):
        # Crear ventana emergente
        register_win = ctk.CTkToplevel(self)
        register_win.title("Registrar Nuevo Empleado")
        register_win.geometry("400x400")
        register_win.grab_set()  # Bloquea la ventana principal hasta cerrar esta

        # Título
        lbl_title = ctk.CTkLabel(register_win, text="Formulario de Registro", font=ctk.CTkFont(size=16, weight="bold"))
        lbl_title.pack(pady=20)

        # Campos de formulario
        entry_name = ctk.CTkEntry(register_win, placeholder_text="Nombre completo")
        entry_name.pack(pady=10, padx=20)

        entry_dni = ctk.CTkEntry(register_win, placeholder_text="DNI")
        entry_dni.pack(pady=10, padx=20)

        entry_cargo = ctk.CTkEntry(register_win, placeholder_text="Cargo")
        entry_cargo.pack(pady=10, padx=20)

        entry_email = ctk.CTkEntry(register_win, placeholder_text="Correo electrónico")
        entry_email.pack(pady=10, padx=20)

        # Botones
        def guardar_empleado():
            nombre = entry_name.get()
            dni = entry_dni.get()
            cargo = entry_cargo.get()
            email = entry_email.get()
            print(f"Empleado registrado: {nombre}, {dni}, {cargo}, {email}")
            register_win.destroy()  # cerrar ventana después de guardar

        btn_save = ctk.CTkButton(register_win, text="Guardar", fg_color="blue", command=guardar_empleado)
        btn_save.pack(pady=15)

        btn_cancel = ctk.CTkButton(register_win, text="Cancelar", fg_color="red", command=register_win.destroy)
        btn_cancel.pack()

    def confirm_logout(self):
        import tkinter.messagebox as mbox
        respuesta = mbox.askokcancel("Cerrar Sesión", "¿Seguro que quieres cerrar sesión?")
        if respuesta:  
            self.logout()   # ✅ Aceptar → cerrar sesión
        else:
            pass            # ❌ Cancelar → no hacer nada

    def confirm_logout(self):
        # Crear ventana emergente
        dialog = ctk.CTkToplevel(self)
        dialog.title("Cerrar Sesión")
        dialog.geometry("300x150")
        dialog.grab_set()  # Bloquear interacción con ventana principal

        # Centrar el diálogo en pantalla
        dialog.update_idletasks()
        x = (dialog.winfo_screenwidth() // 2) - (300 // 2)
        y = (dialog.winfo_screenheight() // 2) - (150 // 2)
        dialog.geometry(f"350x150+{x}+{y}")

        # Texto del mensaje
        lbl = ctk.CTkLabel(dialog, text="¿Seguro que quieres cerrar sesión?", font=ctk.CTkFont(size=14))
        lbl.pack(pady=20)

        # Botones Aceptar / Cancelar
        btn_frame = ctk.CTkFrame(dialog, fg_color="transparent")
        btn_frame.pack(pady=10)

        btn_ok = ctk.CTkButton(btn_frame, text="Aceptar", fg_color="red", hover_color="darkred",
                            command=lambda: (dialog.destroy(), self.logout()))
        btn_ok.grid(row=0, column=0, padx=10)

        btn_cancel = ctk.CTkButton(btn_frame, text="Cancelar", command=dialog.destroy)
        btn_cancel.grid(row=0, column=1, padx=10)

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def change_appearance_mode_event(self, new_appearance_mode):
        ctk.set_appearance_mode(new_appearance_mode)

    def cargar_tabla_empleados(self, pagina):
        # Limpiar tabla anterior
        for widget in self.table_frame.winfo_children():
            widget.destroy()

        # Obtener empleados filtrados
        filtro = self.search_var.get()
        empleados, total_paginas = obtener_empleados(pagina=pagina, por_pagina=10, filtro=filtro)

        # Encabezados
        encabezados = ["ID", "Nombre", "DNI", "Cargo", "Email", "Acciones"]
        for col, text in enumerate(encabezados):
            lbl = ctk.CTkLabel(self.table_frame, text=text, font=ctk.CTkFont(weight="bold"))
            lbl.grid(row=0, column=col, padx=10, pady=5, sticky="w")

        # Filas
        for fila, emp in enumerate(empleados, start=1):
            ctk.CTkLabel(self.table_frame, text=emp["id"]).grid(row=fila, column=0, padx=10, pady=2, sticky="w")
            ctk.CTkLabel(self.table_frame, text=emp["nombre"]).grid(row=fila, column=1, padx=10, pady=2, sticky="w")
            ctk.CTkLabel(self.table_frame, text=emp["dni"]).grid(row=fila, column=2, padx=10, pady=2, sticky="w")
            ctk.CTkLabel(self.table_frame, text=emp["cargo"]).grid(row=fila, column=3, padx=10, pady=2, sticky="w")
            ctk.CTkLabel(self.table_frame, text=emp["email"]).grid(row=fila, column=4, padx=10, pady=2, sticky="w")

            # -------- BOTONES DE ACCIONES --------
            btn_frame = ctk.CTkFrame(self.table_frame, fg_color="transparent")
            btn_frame.grid(row=fila, column=5, padx=10, pady=2)

            btn_update = ctk.CTkButton(btn_frame, text="✏️", width=30, fg_color="blue",
                                    hover_color="darkblue", command=lambda e=emp: self.actualizar_empleado(e))
            btn_update.pack(side="left", padx=2)

            btn_delete = ctk.CTkButton(btn_frame, text="🗑️", width=30, fg_color="red",
                                    hover_color="darkred", command=lambda e=emp: self.eliminar_empleado(e))
            btn_delete.pack(side="left", padx=2)

            btn_photo = ctk.CTkButton(btn_frame, text="📸", width=30, fg_color="orange",
                                    hover_color="darkorange", command=lambda e=emp: self.actualizar_foto(e))
            btn_photo.pack(side="left", padx=2)

        # -------- PAGINACIÓN --------
        for widget in self.pagination_frame.winfo_children():
            widget.destroy()

        if pagina > 1:
            btn_prev = ctk.CTkButton(self.pagination_frame, text="⬅️ Anterior",
                                    command=lambda: self.cargar_tabla_empleados(pagina - 1))
            btn_prev.pack(side="left", padx=5)

        lbl_page = ctk.CTkLabel(self.pagination_frame, text=f"Página {pagina} de {total_paginas}")
        lbl_page.pack(side="left", padx=10)

        if pagina < total_paginas:
            btn_next = ctk.CTkButton(self.pagination_frame, text="Siguiente ➡️",
                                    command=lambda: self.cargar_tabla_empleados(pagina + 1))
            btn_next.pack(side="left", padx=5)

        # Guardar página actual
        self.pagina_actual = pagina

    def actualizar_empleado(self, empleado):
        print(f"✏️ Actualizar empleado: {empleado['nombre']}")

    def eliminar_empleado(self, empleado):
        print(f"🗑️ Eliminar empleado: {empleado['nombre']}")

    def actualizar_foto(self, empleado):
        print(f"📸 Actualizar foto de: {empleado['nombre']}")

    def registro_facial_event(self):
        print("Registro facial iniciado...")


if __name__ == "__main__":
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")
    app = App()
    app.mainloop()
