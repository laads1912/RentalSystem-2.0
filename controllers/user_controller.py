from models.user_model import UserModel

class UserController:
    def __init__(self):
        self.model = UserModel()

    def add_user(self, email, full_name, age, gender, height, weight, shoe_size, is_active, is_employee, password_hash):
        
        # Criar função hash para senha
        
        user_data = (
            email, full_name, age, gender, height, weight, shoe_size, is_active, is_employee, password_hash
        )
        self.model.create_user(user_data)
        print(f'Usuário {full_name} registrado com sucesso.')
