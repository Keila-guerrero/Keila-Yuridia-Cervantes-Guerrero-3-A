from database import crear_conexion

def valida_credenciales(usuario, password):
    try:
        conexion = crear_conexion()
        cursor = conexion.cursor()
        
        query = "SELECT * FROM usuarios WHERE usuario = %s AND password = %s"
        cursor.execute(query, (usuario, password))
        
        resultado = cursor.fetchone()
        cursor.close()
        conexion.close()
        return bool(resultado)
    except Exception as e:
        print(f"Error al validar credenciales: {e}")
    return False

