from database import crear_conexion

def ver_usuarios():
    try:
        conexion = crear_conexion()
        cursor = conexion.cursor()
        
        query = "SELECT id, usuario, rol FROM usuarios"
        cursor.execute(query)
        
        usuarios = cursor.fetchall()
        cursor.close()
        conexion.close()
        return usuarios
    except Exception as e:
        print(f"Error al obtener usuarios: {e}")
    return []

def crear_usuario(usuario, password, rol):
    conexion = crear_conexion()
    if not conexion:
        return False  
    
    try:
        cursor = conexion.cursor()
        query = "INSERT INTO usuarios (usuario, password, rol) VALUES (%s, %s, %s)"
        cursor.execute(query, (usuario, password, rol))
        conexion.commit()
        cursor.close()
        conexion.close()
        return True
    except Exception as e:
        print(f"Error al crear usuario: {e}")
        return False
    
def actualizar_usuario(usuario_id, nuevo_usuario, nuevo_password, nuevo_rol):
    conexion = crear_conexion()
    if not conexion:
        return False  
    
    try:
        cursor = conexion.cursor()
        query = "UPDATE usuarios SET usuario = %s, password = %s, rol = %s WHERE id = %s"
        cursor.execute(query, (nuevo_usuario, nuevo_password, nuevo_rol, usuario_id))
        conexion.commit()
        cursor.close()
        conexion.close()
        return True
    except Exception as e:
        print(f"Error al actualizar usuario: {e}")
        return False
    
def eliminar_usuario(usuario_id):
    conexion = crear_conexion()
    if not conexion:
        return False  
    
    try:
        cursor = conexion.cursor()
        query = "DELETE FROM usuarios WHERE id = %s"
        cursor.execute(query, (usuario_id,))
        conexion.commit()
        cursor.close()
        conexion.close()
        return True
    except Exception as e:
        print(f"Error al eliminar usuario: {e}")
        return False