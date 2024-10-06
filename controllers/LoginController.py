import sqlite3
import bcrypt

from controllers.EmployeeHomeController import EmployeeHomeController
from controllers.RegistrationController import RegistrationController
from views.LoginView import LoginView


class LoginController:
    def __init__(self):
        self.view = LoginView(self)

    def handle_login(self, email, password):
        conn = sqlite3.connect('RentalSystem.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        user = cursor.fetchone()
        if user and bcrypt.checkpw(password.encode(), user[9]):
            self.view.root.withdraw()
            if user[8] == 1:
                self.employee_page(email)
            else:
                self.guest_page(email)
        else:
            self.view.show_message("Login Failed", "Invalid email or password")

    def handle_open_registration(self):
        self.view.root.withdraw()
        registration_controller = RegistrationController(self) 
        registration_controller.open_registration() 
        

    def run(self):
        self.view.mainloop()

    def guest_page(self, email):
        self.view.show_message("Login sucessful", "Chamando página de cliente")
        registration_controller = RegistrationController(self)
        registration_controller.open_home_page(email)

    def employee_page(self, email):
        employee_home_controller = EmployeeHomeController(self)
        employee_home_controller.open_home_page()