import sqlite3
import bcrypt

from controllers.RegisteredUsersController import RegisteredUsersController
from controllers.EmployeeHomeController import EmployeeHomeController
from controllers.RegistrationController import RegistrationController
from views.LoginView import LoginView
from views.RoleSelectionView import RoleSelectionView


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
                RoleSelectionView(self, email).mainloop()
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
        employee_home_controller = EmployeeHomeController(self)
        employee_home_controller.open_user_home_page(email)

    def employee_page(self):
        employee_home_controller = EmployeeHomeController(self)
        employee_home_controller.open_employee_home_page()