from controllers.RegisteredUsersController import RegisteredUsersController
from views.EmployeeHomeView import EmployeeHomeView

class EmployeeHomeController:
    def __init__(self, login_controller):
        self.login_controller = login_controller
        self.view = EmployeeHomeView(self)

    def open_home_page(self):
        self.view.mainloop()

    def open_equipments_page(self):
        pass

    def logout(self):
        self.view.root.withdraw()
        self.login_controller.view.root.deiconify()

    def open_registered_users_page(self):
        registered_users_controller = RegisteredUsersController(self.login_controller)
        self.view.root.withdraw()
        registered_users_controller.registered_users_page()