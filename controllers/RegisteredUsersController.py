from controllers.EmployeeUserEditController import EmployeeUserEditController
from views.RegisteredUsersView import RegisteredUsersView


class RegisteredUsersController:
    def __init__(self, login_controller):
        self.login_controller = login_controller
        self.view = RegisteredUsersView(self)

    def registered_users_page(self):
        self.view.mainloop()

    def open_employee_user_edit_page(self, email):
        employee_user_edit_controller = EmployeeUserEditController()
        self.view.root.withdraw()
        employee_user_edit_controller.employee_user_edit_page(email)