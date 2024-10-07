from controllers.Utils import hash_password
from models.User import User
from views.EmployeeUserEditView import EmployeeUserEditView
from views.RegisteredUsersView import RegisteredUsersView
from views.UserEditView import UserEditView
from views.UserHomeView import UserHomeView


class RegisteredUsersController:
    def __init__(self, controller):
        self.controller = controller
        self.view = None

    def return_home(self):
        self.view.root.withdraw()
        self.controller.employee_page()

    def registered_users_page(self):
        users = User.get_all_users()
        self.view = RegisteredUsersView(self, users)
        self.view.mainloop()

    def open_employee_user_edit_page(self, user):
        self.view.root.withdraw()
        self.view = EmployeeUserEditView(self, user)
        self.view.mainloop()

    def open_user_edit_page(self, email):
        user = User.get_all_user_data(email)
        self.view = UserEditView(self, user)  
        self.view.mainloop()

    def open_user_home_page(self, email):
        self.view = UserHomeView(self, email)
        self.view.root.mainloop(email)

    def log_out(self):
        from controllers.LoginController import LoginController
        self.view.root.destroy()
        login_controller = LoginController()
        login_controller.run()

    def update_user_as_employee(self, email, new_email, full_name, new_password, password_confirmation, gender, shoe_size, age,
                    is_employee, weight, height):
        if self.update_user(email, new_email, full_name, new_password, password_confirmation, gender, shoe_size, age,
                        is_employee, weight, height):
            self.registered_users_page()

    def update_user_as_user(self, email, new_email, full_name, new_password, password_confirmation, gender, shoe_size, age,
                    is_employee, weight, height):
        if self.update_user(email, new_email, full_name, new_password, password_confirmation, gender, shoe_size, age,
                        is_employee, weight, height):
            self.open_user_home_page(email)

    def update_user(self, email, new_email, full_name, new_password, password_confirmation, gender, shoe_size, age,
                    is_employee, weight, height):
        if not new_email or not full_name or not gender or not age or not shoe_size or not weight or not height:
            self.view.show_message("Error", "All fields (except password) are required.")
            return False

        if "@" not in new_email or "." not in new_email.split("@")[-1]:
            self.view.show_message("Error", "Invalid email format.")
            return False

        if not isinstance(age, int) or age <= 0:
            self.view.show_message("Error", "Age must be a positive integer.")
            return False

        if not isinstance(shoe_size, int) or shoe_size <= 0:
            self.view.show_message("Error", "Shoe size must be a positive number.")
            return False

        if not isinstance(weight, int) or weight <= 0:
            self.view.show_message("Error", "Weight must be a positive number.")
            return False

        if not isinstance(height, int) or height <= 0:
            self.view.show_message("Error", "Height must be a positive number.")
            return False

        if new_password:
            if new_password != password_confirmation:
                self.view.show_message("Error", "Password confirmation does not match.")
                return False

            new_password_hash = hash_password(new_password)
        else:
            new_password_hash = None

        User.update_user(email, new_email, full_name, age, gender, height, weight, shoe_size, new_password_hash, is_employee)
        self.view.show_message("Success", "User updated successfully.")
        self.view.root.withdraw() 
        return True

    def delete_user(self, email):
        User.delete_user(email)
        self.view.show_message("Success", "User deleted successfully.")
        self.view.root.withdraw()
        self.registered_users_page()