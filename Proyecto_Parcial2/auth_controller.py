from database import crear_conexion

def valida_credenciales(usuario, password):
    try:
        conexion = crear_conexion()
        cursor = conexion.cursor()
        consulta = "SELECT * FROM usuarios WHERE username = %s AND password = %s"
        cursor.execute(consulta, (usuario, password))
        resultado = cursor.fetchone()
        cursor.close()
        conexion.close()
        return bool(resultado)
    except Exception as e:
        print(f"Error al validar credenciales: {e}")
        return False
