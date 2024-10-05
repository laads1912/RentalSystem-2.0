import sqlite3
import bcrypt

from models.User import User
from views.LoginView import LoginView
from controllers.RegistrationController import RegistrationController

class LoginController:
    def __init__(self):
        self.view = LoginView(self)

    def handle_login(self, email, password):
        conn = sqlite3.connect('RentalSystem.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        user = cursor.fetchone()
        if user and bcrypt.checkpw(password.encode(), user[9]):
            self.view.show_message("Login Successful", f"Welcome, {email}!")
            #aqui vai chamar o controller da página inicial ao invés de mostrar uma mensagem
        else:
            self.view.show_message("Login Failed", "Invalid email or password")

    def handle_open_registration(self):
        self.view.root.withdraw()
        RegistrationController(self)

    def run(self):
        self.view.mainloop()