import bcrypt
from models.User import User
from views.RegistrationView import RegistrationView

class RegistrationController:
    def __init__(self, login_controller):
        self.login_controller = login_controller
        self.view = RegistrationView(self)
        self.view.root.mainloop()

    def hash_password(self, password):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password

    def add_user(self, email, full_name, age, gender, height, weight, shoe_size, password):
        hashed_password = self.hash_password(password)

        User(age, email, full_name, gender, height, hashed_password, shoe_size, weight).create_user()
        
        print(f'Usuário {full_name} registrado com sucesso.')

    def back_to_login(self):
        self.view.close()
        self.login_controller.view.root.deiconify()