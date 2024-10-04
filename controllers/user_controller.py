import bcrypt
from models.user_model import UserModel
from views.user_view import UserView

class UserController:
    def __init__(self, login_controller):
        self.model = UserModel()
        self.login_controller = login_controller
        self.view = UserView(self)
        self.view.root.mainloop()

    def hash_password(self, password):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password

    def add_user(self, email, full_name, age, gender, height, weight, shoe_size, password):
        hashed_password = self.hash_password(password)

        user_data = (
            email, full_name, age, gender, height, weight, shoe_size, True, True, hashed_password
        )
        
        self.model.create_user(user_data)
        print(f'Usuário {full_name} registrado com sucesso.')

    def back_to_login(self):
        self.view.close()
        self.login_controller.view.root.deiconify()