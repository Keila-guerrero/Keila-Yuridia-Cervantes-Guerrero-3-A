import tkinter as tk
from tkinter import ttk, messagebox

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("360x180")
        self.username = None
        self.login_success = tk.BooleanVar(value=False)
        frm = ttk.Frame(self.root, padding=12)
        frm.pack(fill="both", expand=True)
        ttk.Label(frm, text="Usuario:").pack(anchor="w", pady=(0,4))
        self.usuario_entry = ttk.Entry(frm)
        self.usuario_entry.pack(fill="x")
        ttk.Label(frm, text="Contraseña:").pack(anchor="w", pady=(8,4))
        self.password_entry = ttk.Entry(frm, show="*")
        self.password_entry.pack(fill="x")
        btn_frame = ttk.Frame(frm)
        btn_frame.pack(pady=12)
        ttk.Button(btn_frame, text="Ingresar", command=self.intentar_login).pack(side="left", padx=6)
        ttk.Button(btn_frame, text="Salir", command=self.root.destroy).pack(side="left", padx=6)
        self.usuario_entry.focus_set()
        self.root.bind("<Return>", lambda e: self.intentar_login())

    def intentar_login(self):
        usuario = self.usuario_entry.get().strip()
        password = self.password_entry.get().strip()
        if not usuario or not password:
            messagebox.showwarning("Error", "Usuario y contraseña obligatorios")
            return
        # validación básica: acepta cualquier credencial no vacía
        self.username = usuario
        self.login_success.set(True)
