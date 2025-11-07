import mysql.connector
from mysql.connector import Error

def crear_conexion():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='poo_proyect_p2'  
        )

        if conexion.is_connected():
            print("Conexión MySQL exitosa")
            return conexion

    except Error as e:
        print(f" Error al conectar a MySQL: {e}")
        return None

# Ejemplo de uso:
if __name__ == "__main__":
    conexion = crear_conexion()
  