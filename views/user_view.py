import customtkinter as ctk
from tkinter import messagebox
from controllers.user_controller import UserController

class App(ctk.CTk):
    def __init__(self, back_to_login_callback):
        super().__init__()

        self.controller = UserController() 
        self.back_to_login_callback = back_to_login_callback

        self.title("RENTAL SYSTEM")
        self.geometry("800x600")

        
        background_frame = ctk.CTkFrame(self, corner_radius=0, fg_color='white')
        background_frame.place(relwidth=1, relheight=1)

        
        header_frame = ctk.CTkFrame(background_frame, height=50, fg_color='#81c9d8', corner_radius=0)
        header_frame.pack(fill='x')
        header_label = ctk.CTkLabel(header_frame, text="RENTAL SYSTEM", font=('Poppins Medium', 18, 'bold'), text_color="#535353")
        header_label.pack(side='left', padx=10)

        
        cadastro_frame = ctk.CTkFrame(background_frame, corner_radius=10, fg_color="white")
        cadastro_frame.pack(pady=20)
        cadastro_frame.place(relx=0.5, rely=0.5, anchor='center')

        cadastro_label = ctk.CTkLabel(cadastro_frame, text="Cadastro", font=('Poppins Medium', 30, 'bold'), text_color='#8f8e8e')
        cadastro_label.grid(row=0, column=0, columnspan=2, pady=10)

        
        self.entry_email = ctk.CTkEntry(cadastro_frame, placeholder_text="Email", width=220, fg_color='lightgray', border_width=0)
        self.entry_email.grid(row=1, column=0, pady=(10, 10))

        self.entry_name = ctk.CTkEntry(cadastro_frame, placeholder_text="Nome Completo", width=220, fg_color='lightgray', border_width=0)
        self.entry_name.grid(row=2, column=0, pady=(10, 10))

        self.entry_age = ctk.CTkEntry(cadastro_frame, placeholder_text="Idade", width=220, fg_color='lightgray', border_width=0)
        self.entry_age.grid(row=3, column=0, pady=(10, 10))

        self.entry_gender = ctk.CTkEntry(cadastro_frame, placeholder_text="Gênero (MALE/FEMALE)", width=220, fg_color='lightgray', border_width=0)
        self.entry_gender.grid(row=4, column=0, pady=(10, 10))

        self.entry_height = ctk.CTkEntry(cadastro_frame, placeholder_text="Altura (cm)", width=220, fg_color='lightgray', border_width=0)
        self.entry_height.grid(row=5, column=0, pady=(10, 10))

        self.entry_weight = ctk.CTkEntry(cadastro_frame, placeholder_text="Peso (kg)", width=220, fg_color='lightgray', border_width=0)
        self.entry_weight.grid(row=6, column=0, pady=(10, 10))

        self.entry_shoe_size = ctk.CTkEntry(cadastro_frame, placeholder_text="Tamanho do Calçado", width=220, fg_color='lightgray', border_width=0)
        self.entry_shoe_size.grid(row=7, column=0, pady=(10, 10))

        self.entry_password = ctk.CTkEntry(cadastro_frame, placeholder_text="Senha", show='*', width=220, fg_color='lightgray', border_width=0)
        self.entry_password.grid(row=8, column=0, pady=(10, 10))

        self.entry_confirm_password = ctk.CTkEntry(cadastro_frame, placeholder_text="Confirmar Senha", show='*', width=220, fg_color='lightgray', border_width=0)
        self.entry_confirm_password.grid(row=9, column=0, pady=(10, 10))

        
        button_register = ctk.CTkButton(cadastro_frame, text="Criar Conta", font=('Poppins Bold', 13, 'bold'), fg_color='#4094a5', command=self.register_user)
        button_register.grid(row=10, column=0, pady=10)

       
        button_back_to_login = ctk.CTkButton(cadastro_frame, text="Voltar ao Login", font=('Poppins Bold', 13, 'bold'), fg_color='#4094a5', command=self.back_to_login)
        button_back_to_login.grid(row=11, column=0, pady=10)

    def register_user(self):
        
        email = self.entry_email.get()
        full_name = self.entry_name.get()
        age = self.entry_age.get()
        gender = self.entry_gender.get().upper()
        height = self.entry_height.get()
        weight = self.entry_weight.get()
        shoe_size = self.entry_shoe_size.get()
        password = self.entry_password.get()
        confirm_password = self.entry_confirm_password.get()

        
        if not email or not full_name or not age or not gender or not height or not weight or not shoe_size or not password or not confirm_password:
            messagebox.showerror("Erro", "Todos os campos são obrigatórios.")
            return

        if gender not in ['MALE', 'FEMALE']:
            messagebox.showerror("Erro", "Gênero inválido. Use 'MALE' ou 'FEMALE'.")
            return

        if password != confirm_password:
            messagebox.showerror("Erro", "As senhas não coincidem.")
            return

        
        try:
            self.controller.add_user(email, full_name, int(age), gender, int(height), int(weight), int(shoe_size), password)
            messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao cadastrar usuário: {e}")

    def back_to_login(self):
        self.withdraw()
        self.back_to_login_callback()
