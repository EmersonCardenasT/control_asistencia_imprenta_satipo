# utils/empleados_utils.py

empleados_ficticios = [
    {"id": i+1, "nombre": f"Empleado {i+1}", "dni": f"1234567{i:02}", "cargo": "Cargo X", "email": f"empleado{i+1}@correo.com"}
    for i in range(20)
]

def obtener_empleados(pagina=1, por_pagina=10, filtro=""):
    """
    Retorna empleados con filtro y paginación
    """
    # Filtrar por nombre si hay filtro
    if filtro:
        filtrados = [emp for emp in empleados_ficticios if filtro.lower() in emp["nombre"].lower()]
    else:
        filtrados = empleados_ficticios

    # Calcular paginación
    inicio = (pagina - 1) * por_pagina
    fin = inicio + por_pagina
    empleados_pagina = filtrados[inicio:fin]

    total_paginas = (len(filtrados) + por_pagina - 1) // por_pagina

    return empleados_pagina, total_paginas
