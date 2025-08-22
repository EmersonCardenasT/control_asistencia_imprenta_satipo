from database.connection import create_connection

def obtener_empleados(pagina=1, por_pagina=10, filtro=""):
    """Obtiene empleados con paginación y filtro opcional"""
    conn = create_connection()
    if not conn:
        return [], 0

    cursor = conn.cursor(dictionary=True)

    # Construcción de query con filtro
    where = f"WHERE nombre LIKE '%{filtro}%' OR apellido LIKE '%{filtro}%'" if filtro else ""
    
    # Total de registros
    cursor.execute(f"SELECT COUNT(*) as total FROM empleados {where}")
    total = cursor.fetchone()["total"]
    total_paginas = (total // por_pagina) + (1 if total % por_pagina > 0 else 0)

    # Paginación
    offset = (pagina - 1) * por_pagina
    query = f"""
        SELECT id, foto, nombre, apellido, dni, telefono, genero, fecha_nacimiento,
               direccion, email, cargo_id, estado, created_at, updated_at
        FROM empleados
        {where}
        ORDER BY id DESC
        LIMIT {por_pagina} OFFSET {offset}
    """
    cursor.execute(query)
    empleados = cursor.fetchall()

    cursor.close()
    conn.close()
    return empleados, total_paginas
