from models.user_model import UserModel
from views.login_view import LoginView

class LoginController:
    def __init__(self):
        self.model = UserModel()
        self.view = LoginView(self)

    def handle_login(self, email, password):
        if self.model.validate_user(email, password):
            self.view.show_message("Login Successful", f"Welcome, {email}!")
        else:
            self.view.show_message("Login Failed", "Invalid email or password")

    def run(self):
        self.view.mainloop()
