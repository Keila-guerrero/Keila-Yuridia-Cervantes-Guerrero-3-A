import tkinter as tk
from tkinter import messagebox, ttk, scrolledtext
from productos_controller import ver_productos, crear_producto, actualizar_producto, eliminar_producto


class DashboardApp:
    def __init__(self, username):
        self.username = username
        self.root = tk.Tk()
        self.root.title(f"Dashboard - {username}")
        self.root.geometry("1000x650")
        self.root.resizable(True, True)

        self.crear_elementos()
        self.actualizar_lista_productos()
        self.root.mainloop()

    def crear_elementos(self):
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        tk.Label(main_frame, text=f"¡Bienvenido al Dashboard, {self.username}!",
                 font=("Arial", 16, "bold")).pack(pady=10)

        button_frame = tk.Frame(main_frame)
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Actualizar lista", width=15,
                  command=self.actualizar_lista_productos).pack(side=tk.LEFT, padx=5)

        tk.Button(button_frame, text="Agregar producto", width=15,
                  command=self.agregar_producto).pack(side=tk.LEFT, padx=5)

        tk.Button(button_frame, text="Editar producto", width=15,
                  command=self.editar_producto).pack(side=tk.LEFT, padx=5)

        tk.Button(button_frame, text="Eliminar producto", width=15,
                  command=self.eliminar_producto).pack(side=tk.LEFT, padx=5)

        tk.Button(button_frame, text="Cerrar sesión", width=15,
                  command=self.cerrar_sesion).pack(side=tk.LEFT, padx=5)

        cols = ("ID", "Nombre", "Stock", "Precio", "Status", "Marca", "Proveedor", "Descripción")
        self.tree = ttk.Treeview(main_frame, columns=cols, show="headings", height=15)
        for col in cols:
            self.tree.heading(col, text=col)

        self.tree.column("ID", width=60)
        self.tree.column("Nombre", width=220)
        self.tree.column("Stock", width=80, anchor="center")
        self.tree.column("Precio", width=100, anchor="e")
        self.tree.column("Status", width=90, anchor="center")
        self.tree.column("Marca", width=120)
        self.tree.column("Proveedor", width=140)
        self.tree.column("Descripción", width=260)

        self.tree.pack(fill="both", expand=True, pady=10)

        scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=scrollbar.set)

    def actualizar_lista_productos(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        productos = ver_productos()
        if productos:
            for p in productos:
                # asumo orden: id_producto, nombre_producto, stock, precio, status, marca, proveedor, descripcion
                self.tree.insert("", "end", values=p)
        else:
            messagebox.showwarning("Sin datos", "No se pudieron cargar los productos o la lista está vacía.")

    def agregar_producto(self):
        self.mostrar_formulario_producto("Agregar Producto")

    def editar_producto(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Selección requerida", "Por favor selecciona un producto para editar.")
            return

        producto_data = self.tree.item(seleccion[0], "values")
        self.mostrar_formulario_producto("Editar Producto", producto_data)

    def eliminar_producto(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Selección requerida", "Por favor selecciona un producto para eliminar.")
            return

        producto_data = self.tree.item(seleccion[0], "values")
        producto_id = producto_data[0]
        producto_nombre = producto_data[1]

        respuesta = messagebox.askyesno(
            "Confirmar eliminación",
            f"¿Estás seguro de que deseas eliminar el producto '{producto_nombre}'?"
        )

        if respuesta:
            if eliminar_producto(producto_id):
                messagebox.showinfo("Éxito", "Producto eliminado correctamente.")
                self.actualizar_lista_productos()
            else:
                messagebox.showerror("Error", "No se pudo eliminar el producto.")

    def mostrar_formulario_producto(self, titulo, producto_data=None):
        formulario = tk.Toplevel(self.root)
        formulario.title(titulo)
        formulario.geometry("520x520")
        formulario.resizable(False, False)
        formulario.transient(self.root)
        formulario.grab_set()

        frm = tk.Frame(formulario)
        frm.pack(padx=12, pady=12, fill="both", expand=True)

        def campo(label_text):
            tk.Label(frm, text=label_text, font=("Arial", 10)).pack(anchor="w", pady=(6, 0))
            e = tk.Entry(frm, width=60)
            e.pack(pady=2, fill="x")
            return e

        nombre_entry = campo("Nombre:")
        stock_entry = campo("Stock (número):")
        precio_entry = campo("Precio (ej. 199.99):")
        status_entry = campo("Status (activo/inactivo):")
        marca_entry = campo("Marca:")
        proveedor_entry = campo("Proveedor:")

        tk.Label(frm, text="Descripción:", font=("Arial", 10)).pack(anchor="w", pady=(6, 0))
        descripcion_text = scrolledtext.ScrolledText(frm, width=60, height=6, wrap="word")
        descripcion_text.pack(pady=4, fill="both", expand=False)

        if producto_data:
            try:
                nombre_entry.insert(0, producto_data[1])
                stock_entry.insert(0, producto_data[2])
                precio_entry.insert(0, producto_data[3])
                status_entry.insert(0, producto_data[4])
                marca_entry.insert(0, producto_data[5])
                proveedor_entry.insert(0, producto_data[6])
                descripcion_text.insert("1.0", producto_data[7] if len(producto_data) > 7 else "")
            except Exception:
                pass

        def guardar_producto():
            nombre = nombre_entry.get().strip()
            stock_s = stock_entry.get().strip()
            precio_s = precio_entry.get().strip()
            status = status_entry.get().strip()
            marca = marca_entry.get().strip()
            proveedor = proveedor_entry.get().strip()
            descripcion = descripcion_text.get("1.0", "end").strip()

            if not nombre:
                messagebox.showwarning("Datos incompletos", "El nombre del producto es obligatorio.")
                return

            try:
                stock = int(stock_s) if stock_s != "" else 0
            except ValueError:
                messagebox.showwarning("Tipo incorrecto", "Stock debe ser un número entero.")
                return

            try:
                precio = float(precio_s) if precio_s != "" else 0.0
            except ValueError:
                messagebox.showwarning("Tipo incorrecto", "Precio debe ser un número (uso de punto decimal).")
                return

            if producto_data:
                producto_id = producto_data[0]
                if actualizar_producto(producto_id, nombre, stock, precio, status, marca, proveedor, descripcion):
                    messagebox.showinfo("Éxito", "Producto actualizado correctamente.")
                    formulario.destroy()
                    self.actualizar_lista_productos()
                else:
                    messagebox.showerror("Error", "No se pudo actualizar el producto.")
            else:
                if crear_producto(nombre, stock, precio, status, marca, proveedor, descripcion):
                    messagebox.showinfo("Éxito", "Producto creado correctamente.")
                    formulario.destroy()
                    self.actualizar_lista_productos()
                else:
                    messagebox.showerror("Error", "No se pudo crear el producto.")

        tk.Button(frm, text="Guardar", width=15, command=guardar_producto).pack(pady=20)
        tk.Button(frm, text="Cancelar", width=15, command=formulario.destroy).pack(pady=5)

    def cerrar_sesion(self):
        self.root.destroy()
        messagebox.showinfo("Cerrar sesión", "Has cerrado sesión correctamente.")


if __name__ == "__main__":
    app = DashboardApp("admin")
