from database import crear_conexion

def ver_productos():
    try:
        conexion = crear_conexion()
        if not conexion:
            return []
        cursor = conexion.cursor()
        query = "SELECT id_producto, nombre_producto, stock, precio, status, marca, proveedor, descripcion FROM productos"
        cursor.execute(query)
        filas = cursor.fetchall()
        cursor.close()
        conexion.close()
        return filas
    except Exception as e:
        print("Error ver_productos:", e)
        return []

def crear_producto(nombre_producto, stock, precio, status, marca, proveedor, descripcion):
    conexion = crear_conexion()
    if not conexion:
        return False
    try:
        cursor = conexion.cursor()
        query = """INSERT INTO productos
                   (nombre_producto, stock, precio, status, marca, proveedor, descripcion)
                   VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(query, (nombre_producto, stock, precio, status, marca, proveedor, descripcion))
        conexion.commit()
        cursor.close()
        conexion.close()
        return True
    except Exception as e:
        print("Error crear_producto:", e)
        return False

def actualizar_producto(id_producto, nombre_producto, stock, precio, status, marca, proveedor, descripcion):
    conexion = crear_conexion()
    if not conexion:
        return False
    try:
        cursor = conexion.cursor()
        query = """UPDATE productos
                   SET nombre_producto=%s, stock=%s, precio=%s, status=%s,
                       marca=%s, proveedor=%s, descripcion=%s
                   WHERE id_producto=%s"""
        cursor.execute(query, (nombre_producto, stock, precio, status, marca, proveedor, descripcion, id_producto))
        conexion.commit()
        afectadas = cursor.rowcount
        cursor.close()
        conexion.close()
        return afectadas > 0
    except Exception as e:
        print("Error actualizar_producto:", e)
        return False

def eliminar_producto(id_producto):
    conexion = crear_conexion()
    if not conexion:
        return False
    try:
        cursor = conexion.cursor()
        query = "DELETE FROM productos WHERE id_producto = %s"
        cursor.execute(query, (id_producto,))
        conexion.commit()
        afectadas = cursor.rowcount
        cursor.close()
        conexion.close()
        return afectadas > 0
    except Exception as e:
        print("Error eliminar_producto:", e)
        return False
