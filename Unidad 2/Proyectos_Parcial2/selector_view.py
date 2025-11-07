import tkinter as tk

class SelectorApp:
    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.root.title("Selector de módulo")
        self.root.geometry("320x140")
        self.crear_gui()

    def crear_gui(self):
        tk.Label(self.root, text=f"Bienvenido, {self.username}", font=("Arial", 12, "bold")).pack(pady=8)
        tk.Label(self.root, text="Selecciona el módulo:").pack(pady=(0,8))
        frame = tk.Frame(self.root)
        frame.pack()
        tk.Button(frame, text="Productos", width=12, command=self.abrir_productos).pack(side="left", padx=8)
        tk.Button(frame, text="Usuarios", width=12, command=self.abrir_usuarios).pack(side="left", padx=8)

    def abrir_productos(self):
        self.root.destroy()
        from productos_view import DashboardApp as ProductosDashboard
        ProductosDashboard(self.username)

    def abrir_usuarios(self):
        self.root.destroy()
        from dashboard_view import DashboardApp as UsuariosDashboard
        UsuariosDashboard(self.username)
