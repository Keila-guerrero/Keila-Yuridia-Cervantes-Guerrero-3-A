import tkinter as tk
from tkinter import messagebox

class DashboardApp:
    def __init__(self, username):
        self.username = username
        self.root = tk.Tk()
        self.root.title(f"Bienvenido, {username}")
        self.root.geometry("600x450")
        self.root.resizable(True, True)
        self.crear_elementos()
        self.root.mainloop()
    
    def crear_elementos(self):
        tk.Button(self.root, text="Agregar usuario", width=20, command=self.agregar_usuario).pack(pady=10)
        tk.Button(self.root, text="Ver usuarios", width=20, command=self.ver_usuarios).pack(pady=10)
        tk.Button(self.root, text="Actualizar usuario", width=20, command=self.actualizar_usuario).pack(pady=10)
        tk.Button(self.root, text="Eliminar usuario", width=20, command=self.eliminar_usuario).pack(pady=10)
        tk.Button(self.root, text="Cerrar Sesión", width=20, command=self.cerrar_sesion, bg="salmon").pack(pady=30)
        
    def agregar_usuario(self):
        messagebox.showinfo("Información", "Función para AGREGAR un nuevo usuario.")

    def ver_usuarios(self):
        messagebox.showinfo("Información", "Función para VER los usuarios existentes.")

    def actualizar_usuario(self):
        messagebox.showinfo("Información", "Función para ACTUALIZAR un usuario.")

    def eliminar_usuario(self):
        if messagebox.askokcancel("Confirmar", "¿Estás seguro de que quieres eliminar un usuario?"):
            messagebox.showinfo("Información", "Función para ELIMINAR un usuario.")

    def cerrar_sesion(self):
        if messagebox.askokcancel("Cerrar Sesión", "¿Estás seguro de que quieres salir?"):
            self.root.destroy()

if __name__ == "__main__":
    nombre_de_usuario = "Admin"
    app = DashboardApp(nombre_de_usuario)
        

