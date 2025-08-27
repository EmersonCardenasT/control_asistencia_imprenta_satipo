import mysql.connector
from mysql.connector import Error

def create_connection():
    """Crea y retorna una conexión a la base de datos MySQL"""
    try:
        connection = mysql.connector.connect(
            host="localhost",        # Cambia si usas otro host
            user="root",             # Tu usuario
            password="",     
            port=3308,               # Puerto por defecto de MySQL
            # Puerto por defecto de MySQL

            database="asistencia_facial_imprenta_satipo"  # Tu base de datos
        )
        if connection.is_connected():
            print("✅ Conexión exitosa a la base de datos")
            return connection
    except Error as e:
        print(f"❌ Error al conectar a MySQL: {e}")
        return None
