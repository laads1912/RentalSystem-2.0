import bcrypt
from models.User import User
from views.HomeView import HomeView
from views.UserEditView import UserEditView
from views.RegistrationView import RegistrationView

class RegistrationController:
    def __init__(self, login_controller):
        self.login_controller = login_controller


    def hash_password(self, password):
        salt = bcrypt.gensalt()
        password_hash = bcrypt.hashpw(password.encode('utf-8'), salt)
        return password_hash

    def add_user(self, email, full_name, age, gender, height, weight, shoe_size, password):
        password_hash = self.hash_password(password)

        User(age, email, full_name, gender, height, password_hash, shoe_size, weight).create_user()
        print(f'Usuário {full_name} registrado com sucesso.')
     
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
        print(f'Usuário atualizado com sucesso.')

    def back_to_login(self):
        self.view.close()
        self.login_controller.view.root.deiconify()