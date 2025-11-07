import tkinter as tk
from tkinter import messagebox, ttk
from user_controller import ver_usuarios, crear_usuario, actualizar_usuario, eliminar_usuario


class DashboardApp:
    def __init__(self, username):
        self.username = username
        self.root = tk.Tk()
        self.root.title(f"Dashboard - {username}")
        self.root.geometry("800x600")   
        self.root.resizable(True, True)
        
        self.crear_elementos()
        self.actualizar_lista_usuarios()
        self.root.mainloop()
        
    def crear_elementos(self):
        # Frame principal
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Título
        tk.Label(main_frame, text=f"¡Bienvenido al Dashboard, {self.username}!", 
                font=("Arial", 16, "bold")).pack(pady=10)
        
        # Frame para botones
        button_frame = tk.Frame(main_frame)
        button_frame.pack(pady=10)
        
        tk.Button(button_frame, text="Actualizar lista", width=15, 
                 command=self.actualizar_lista_usuarios).pack(side=tk.LEFT, padx=5)
        
        tk.Button(button_frame, text="Agregar usuario", width=15, 
                 command=self.agregar_usuario).pack(side=tk.LEFT, padx=5)
        
        tk.Button(button_frame, text="Editar usuario", width=15, 
                 command=self.editar_usuario).pack(side=tk.LEFT, padx=5)
        
        tk.Button(button_frame, text="Eliminar usuario", width=15, 
                 command=self.eliminar_usuario).pack(side=tk.LEFT, padx=5)
        
        tk.Button(button_frame, text="Cerrar sesión", width=15, 
                 command=self.cerrar_sesion).pack(side=tk.LEFT, padx=5)
        
        # Treeview para mostrar usuarios
        self.tree = ttk.Treeview(main_frame, columns=("ID", "Usuario", "Rol"), show="headings", height=15)
        self.tree.heading("ID", text="ID")
        self.tree.heading("Usuario", text="Nombre de usuario")
        self.tree.heading("Rol", text="Rol")
        
        self.tree.column("ID", width=50)
        self.tree.column("Usuario", width=200)
        self.tree.column("Rol", width=100)
        
        self.tree.pack(fill="both", expand=True, pady=10)
        
        # Scrollbar para el treeview
        scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=scrollbar.set)
        
    def actualizar_lista_usuarios(self):
        # Limpiar treeview
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        # Obtener y mostrar usuarios
        usuarios = ver_usuarios()
        if usuarios:
            for usuario in usuarios:
                self.tree.insert("", "end", values=usuario)
        else:
            messagebox.showwarning("Sin datos", "No se pudieron cargar los usuarios.")
        
    def agregar_usuario(self):
        self.mostrar_formulario_usuario("Agregar Usuario")
        
    def editar_usuario(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Selección requerida", "Por favor selecciona un usuario para editar.")
            return
            
        usuario_data = self.tree.item(seleccion[0], "values")
        self.mostrar_formulario_usuario("Editar Usuario", usuario_data)
        
    def eliminar_usuario(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Selección requerida", "Por favor selecciona un usuario para eliminar.")
            return
            
        usuario_data = self.tree.item(seleccion[0], "values")
        usuario_id = usuario_data[0]
        usuario_nombre = usuario_data[1]
        
        respuesta = messagebox.askyesno(
            "Confirmar eliminación", 
            f"¿Estás seguro de que deseas eliminar al usuario '{usuario_nombre}'?"
        )
        
        if respuesta:
            if eliminar_usuario(usuario_id):
                messagebox.showinfo("Éxito", "Usuario eliminado correctamente.")
                self.actualizar_lista_usuarios()
            else:
                messagebox.showerror("Error", "No se pudo eliminar el usuario.")
        
    def mostrar_formulario_usuario(self, titulo, usuario_data=None):
        formulario = tk.Toplevel(self.root)
        formulario.title(titulo)
        formulario.geometry("400x300")
        formulario.resizable(False, False)
        formulario.transient(self.root)
        formulario.grab_set()
        
        # Campos del formulario
        tk.Label(formulario, text="Usuario:", font=("Arial", 10)).pack(pady=5)
        usuario_entry = tk.Entry(formulario, width=30)
        usuario_entry.pack(pady=5)
        
        tk.Label(formulario, text="Contraseña:", font=("Arial", 10)).pack(pady=5)
        password_entry = tk.Entry(formulario, width=30, show="*")
        password_entry.pack(pady=5)
        
        tk.Label(formulario, text="Rol:", font=("Arial", 10)).pack(pady=5)
        rol_entry = tk.Entry(formulario, width=30)
        rol_entry.pack(pady=5)
        
        # Si estamos editando, llenar los campos
        if usuario_data:
            usuario_entry.insert(0, usuario_data[1])
            rol_entry.insert(0, usuario_data[2])
            # Para edición, la contraseña se deja en blanco para cambiarla opcionalmente
        
        def guardar_usuario():
            usuario = usuario_entry.get().strip()
            password = password_entry.get().strip()
            rol = rol_entry.get().strip()
            
            if not usuario or not rol:
                messagebox.showwarning("Datos incompletos", "Usuario y rol son obligatorios.")
                return
                
            if usuario_data:  # Modo edición
                if not password:  # Si no se cambia la contraseña, mantener la actual
                    # En una aplicación real, aquí buscarías la contraseña actual de la BD
                    messagebox.showwarning("Contraseña requerida", "Para editar se requiere contraseña.")
                    return
                    
                if actualizar_usuario(usuario_data[0], usuario, password, rol):
                    messagebox.showinfo("Éxito", "Usuario actualizado correctamente.")
                    formulario.destroy()
                    self.actualizar_lista_usuarios()
                else:
                    messagebox.showerror("Error", "No se pudo actualizar el usuario.")
            else:  # Modo creación
                if not password:
                    messagebox.showwarning("Contraseña requerida", "La contraseña es obligatoria para nuevo usuario.")
                    return
                    
                if crear_usuario(usuario, password, rol):
                    messagebox.showinfo("Éxito", "Usuario creado correctamente.")
                    formulario.destroy()
                    self.actualizar_lista_usuarios()
                else:
                    messagebox.showerror("Error", "No se pudo crear el usuario.")
        
        tk.Button(formulario, text="Guardar", width=15, command=guardar_usuario).pack(pady=20)
        tk.Button(formulario, text="Cancelar", width=15, command=formulario.destroy).pack(pady=5)
        
    def cerrar_sesion(self):
        self.root.destroy()
        messagebox.showinfo("Cerrar sesión", "Has cerrado sesión correctamente.")
    
    
if __name__ == "__main__":
    app = DashboardApp("admin")