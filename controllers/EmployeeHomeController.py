from controllers.RegisteredUsersController import RegisteredUsersController
from views.EmployeeHomeView import EmployeeHomeView

class EmployeeHomeController:
    def __init__(self, login_controller):
        self.login_controller = login_controller
        self.view = EmployeeHomeView(self)

    def open_home_page(self):
        self.view.mainloop()

    def open_registered_users_page(self):
        registered_users_controller = RegisteredUsersController(self)
        self.view.root.withdraw()
        registered_users_controller.registered_users_page()