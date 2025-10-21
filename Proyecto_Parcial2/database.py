import mysql.connector
from mysql.connector import Error

def crear_conexion():
    conexion = None
    try:
        conexion = mysql.connector.connect(
            host = "localhost",
            user = 'root',
            password = '',
            database = 'POO_project_P2'
        )
            
            
        
        if conexion.is_connected():
            print("Conexion a la base exitosa")
            
    except Error as e:
        print(f"Error al conectar d tipo {e} ")
    
    
    return conexion
def close_connection(connection):
    """Cierra la conexión a la base de datos."""
    if connection and connection.is_connected():
        connection.close()
        print("Conexión a MySQL cerrada.")


# Ejemplo de uso:
if __name__ == "__main__":
    conexion = crear_conexion()
    if conexion:
        conexion.close()
        print ("Conexión cerrada correctamente.")
