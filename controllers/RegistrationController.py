import bcrypt
from models.User import User
from views.HomeView import HomeView
from views.UserEditView import UserEditView
from views.RegistrationView import RegistrationView

class RegistrationController:
    def __init__(self, login_controller):
        self.login_controller = login_controller
        self.registration_view = RegistrationView(self)

    def hash_password(self, password):
        salt = bcrypt.gensalt()
        password_hash = bcrypt.hashpw(password.encode('utf-8'), salt)
        return password_hash

    def add_user(self, email, full_name, age, gender, height, weight, shoe_size, password, confirm_password):
        if not all([email, full_name, age, gender, height, weight, shoe_size, password, confirm_password]):
            self.registration_view.message_box("Error", "Please fill in all fields.")
            return

        if '@' not in email or '.' not in email.split('@')[-1]:
            self.registration_view.message_box("Error", "Invalid email.")
            return

        if password != confirm_password:
            self.registration_view.message_box("Error", "Passwords do not match.")
            return

        if not str(age).isnumeric() or int(age) < 0 or int(age) > 120:
            self.registration_view.message_box("Error", "Invalid age.")
            return

        if not str(height).isnumeric() or int(height) < 0 or int(height) > 300:
            self.registration_view.message_box("Error", "Invalid height.")
            return

        if not str(weight).isnumeric() or int(weight) < 0 or int(weight) > 300:
            self.registration_view.message_box("Error", "Invalid weight.")
            return

        if not str(shoe_size).isnumeric() or int(shoe_size) < 0 or int(shoe_size) > 50:
            self.registration_view.message_box("Error", "Invalid shoe size.")
            return

        password_hash = self.hash_password(password)
        try:
            User(int(age), email, full_name, gender, int(height), password_hash, int(shoe_size), int(weight)).create_user()
            self.registration_view.message_box("Success", "User registered successfully.")
            self.back_to_login()
        except Exception as e:
            self.registration_view.message_box("Error", f"Error registering user: {str(e)}")
            return

    def open_registration(self):
        self.view = RegistrationView(self)
        self.view.root.mainloop()
    
    def open_edit_user(self, email):
        user = User.get_all_user_data(email)
        self.view = UserEditView(self, user)
        self.view.root.mainloop()
    
    def open_home_page(self, email):
        self.view = HomeView(self, email)
        self.view.root.mainloop()

    def update_user(self, email, full_name, age, gender, height, weight, shoe_size, password=None):
        if password:
            password_hash = self.hash_password(password)
        else:
            password_hash = None  

        User.update_user(email, full_name, age, gender, height, weight, shoe_size, password_hash)
        print(f'User updated successfully.')

    def back_to_login(self):
        self.view.close()
        self.login_controller.view.root.deiconify()