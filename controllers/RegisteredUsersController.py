from views.EmployeeUserEditView import EmployeeUserEditView
from views.RegisteredUsersView import RegisteredUsersView


class RegisteredUsersController:
    def __init__(self):
        self.view = None

    def registered_users_page(self):
        # TODO: get all users and pass to RegisteredUsersView
        self.view = RegisteredUsersView(self)
        self.view.mainloop()

    def open_employee_user_edit_page(self, email):
        # TODO: get user by email and pass to EmployeeUserEditView
        self.view.root.withdraw()
        EmployeeUserEditView(self).mainloop()