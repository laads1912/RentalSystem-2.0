from controllers.RegisteredUsersController import RegisteredUsersController
from views.EmployeeHomeView import EmployeeHomeView
from views.UserHomeView import UserHomeView

class EmployeeHomeController:
    def __init__(self, login_controller):
        self.login_controller = login_controller

    def open_employee_home_page(self):
        self.view = EmployeeHomeView(self)
        self.view.mainloop()
    
    def open_user_home_page(self, email):
        self.view = UserHomeView(self, email)
        self.view.mainloop(email)

    def open_equipments_page(self):
        pass

    def logout(self):
        self.view.root.withdraw()
        self.login_controller.view.root.deiconify()

    def open_registered_users_page(self):
        registered_users_controller = RegisteredUsersController(self.login_controller)
        self.view.root.withdraw()
        registered_users_controller.registered_users_page()
    
    def open_user_edit_page(self, email):
        registered_users_controller = RegisteredUsersController(self.login_controller)
        registered_users_controller.user_edit_page(email)