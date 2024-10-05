import sqlite3

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
        
        """if self.model.validate_user(email, password):
            self.view.show_message("Login Successful", f"Welcome, {email}!")
        else:
            self.view.show_message("Login Failed", "Invalid email or password")"""

    def handle_open_registration(self):
        self.view.root.withdraw()
        RegistrationController(self)

    def run(self):
        self.view.mainloop()