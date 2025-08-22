import customtkinter as ctk
from database.empleados import obtener_empleados

def render_tabla_empleados(self, pagina):
    # Limpiar tabla anterior
    for widget in self.table_frame.winfo_children():
        widget.destroy()

    # Obtener empleados
    filtro = self.search_var.get()
    empleados, total_paginas = obtener_empleados(pagina=pagina, por_pagina=10, filtro=filtro)

    # Encabezados
    encabezados = [
        "ID", "Foto", "Nombre", "Apellido", "DNI", "Teléfono", "Género", "Fecha Nac.",
        "Dirección", "Email", "Cargo ID", "Estado", "Creado", "Actualizado", "Acciones"
    ]
    for col, text in enumerate(encabezados):
        lbl = ctk.CTkLabel(self.table_frame, text=text, font=ctk.CTkFont(weight="bold"))
        lbl.grid(row=0, column=col, padx=8, pady=5, sticky="w")

    # Filas
    for fila, emp in enumerate(empleados, start=1):
        ctk.CTkLabel(self.table_frame, text=emp["id"]).grid(row=fila, column=0, padx=8, pady=2, sticky="w")
        ctk.CTkLabel(self.table_frame, text="📷").grid(row=fila, column=1, padx=8, pady=2, sticky="w")  # TODO: mostrar imagen real

        ctk.CTkLabel(self.table_frame, text=emp["nombre"]).grid(row=fila, column=2, padx=8, pady=2, sticky="w")
        ctk.CTkLabel(self.table_frame, text=emp["apellido"]).grid(row=fila, column=3, padx=8, pady=2, sticky="w")
        ctk.CTkLabel(self.table_frame, text=emp["dni"]).grid(row=fila, column=4, padx=8, pady=2, sticky="w")
        ctk.CTkLabel(self.table_frame, text=emp["telefono"]).grid(row=fila, column=5, padx=8, pady=2, sticky="w")
        ctk.CTkLabel(self.table_frame, text=emp["genero"]).grid(row=fila, column=6, padx=8, pady=2, sticky="w")
        ctk.CTkLabel(self.table_frame, text=str(emp["fecha_nacimiento"])).grid(row=fila, column=7, padx=8, pady=2, sticky="w")
        ctk.CTkLabel(self.table_frame, text=emp["direccion"]).grid(row=fila, column=8, padx=8, pady=2, sticky="w")
        ctk.CTkLabel(self.table_frame, text=emp["email"]).grid(row=fila, column=9, padx=8, pady=2, sticky="w")
        ctk.CTkLabel(self.table_frame, text=emp["cargo_id"]).grid(row=fila, column=10, padx=8, pady=2, sticky="w")
        ctk.CTkLabel(self.table_frame, text=emp["estado"]).grid(row=fila, column=11, padx=8, pady=2, sticky="w")
        ctk.CTkLabel(self.table_frame, text=str(emp["created_at"])).grid(row=fila, column=12, padx=8, pady=2, sticky="w")
        ctk.CTkLabel(self.table_frame, text=str(emp["updated_at"])).grid(row=fila, column=13, padx=8, pady=2, sticky="w")

        # -------- BOTONES DE ACCIONES --------
        btn_frame = ctk.CTkFrame(self.table_frame, fg_color="transparent")
        btn_frame.grid(row=fila, column=14, padx=5, pady=2)

        ctk.CTkButton(btn_frame, text="✏️", width=30, fg_color="blue",
                      command=lambda e=emp: self.actualizar_empleado(e)).pack(side="left", padx=2)
        ctk.CTkButton(btn_frame, text="🗑️", width=30, fg_color="red",
                      command=lambda e=emp: self.eliminar_empleado(e)).pack(side="left", padx=2)
        ctk.CTkButton(btn_frame, text="📸", width=30, fg_color="orange",
                      command=lambda e=emp: self.actualizar_foto(e)).pack(side="left", padx=2)

    # -------- PAGINACIÓN --------
    for widget in self.pagination_frame.winfo_children():
        widget.destroy()

    if pagina > 1:
        ctk.CTkButton(self.pagination_frame, text="⬅️ Anterior",
                      command=lambda: render_tabla_empleados(self, pagina - 1)).pack(side="left", padx=5)

    lbl_page = ctk.CTkLabel(self.pagination_frame, text=f"Página {pagina} de {total_paginas}")
    lbl_page.pack(side="left", padx=10)

    if pagina < total_paginas:
        ctk.CTkButton(self.pagination_frame, text="Siguiente ➡️",
                      command=lambda: render_tabla_empleados(self, pagina + 1)).pack(side="left", padx=5)

    self.pagina_actual = pagina
