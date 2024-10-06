from views.EmployeeUserEditView import EmployeeUserEditView


class EmployeeUserEditController:
    def __init__(self):
        self.view = EmployeeUserEditView(self)

    def employee_user_edit_page(self, email):
        self.view.mainloop()