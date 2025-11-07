from tkinter import Tk
from login_view import LoginApp
from selector_view import SelectorApp

def on_login_success(username, login_root):
    login_root.destroy()
    root = Tk()
    SelectorApp(root, username)
    root.mainloop()

if __name__ == "__main__":
    root = Tk()
    app = LoginApp(root)
    root.wait_variable(app.login_success)
    if app.login_success.get():
        on_login_success(app.username, root)
