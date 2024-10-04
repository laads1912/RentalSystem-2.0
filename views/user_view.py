import customtkinter as ctk
from tkinter import messagebox

class UserView:
    def __init__(self, controller):
        self.controller = controller
        self.root = ctk.CTk()
        self.root.title("RENTAL SYSTEM - Create Account")
        self.root.geometry("1000x700")

        background_frame = ctk.CTkFrame(self.root, corner_radius=0, fg_color='white')
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

        label_email = ctk.CTkLabel(cadastro_frame, text="EMAIL", font=('DM Sans', 10), text_color='#8f8e8e')
        label_email.grid(row=1, column=0, sticky='w', pady=(5, 2))
        self.entry_email = ctk.CTkEntry(cadastro_frame, placeholder_text="Email", width=220, fg_color='lightgray', border_width=0)
        self.entry_email.grid(row=2, column=0, pady=(0, 10))

        label_name = ctk.CTkLabel(cadastro_frame, text="NOME COMPLETO", font=('DM Sans', 10), text_color='#8f8e8e')
        label_name.grid(row=3, column=0, sticky='w', pady=(5, 2))
        self.entry_name = ctk.CTkEntry(cadastro_frame, placeholder_text="Nome Completo", width=220, fg_color='lightgray', border_width=0)
        self.entry_name.grid(row=4, column=0, pady=(0, 10))

        label_age = ctk.CTkLabel(cadastro_frame, text="IDADE", font=('DM Sans', 10), text_color='#8f8e8e')
        label_age.grid(row=5, column=0, sticky='w', pady=(5, 2))
        self.entry_age = ctk.CTkEntry(cadastro_frame, placeholder_text="Idade", width=220, fg_color='lightgray', border_width=0)
        self.entry_age.grid(row=6, column=0, pady=(0, 10))

        label_gender = ctk.CTkLabel(cadastro_frame, text="GÊNERO", font=('DM Sans', 10), text_color='#8f8e8e')
        label_gender.grid(row=7, column=0, sticky='w', pady=(5, 2))
        self.entry_gender = ctk.CTkEntry(cadastro_frame, placeholder_text="Gênero (MALE/FEMALE)", width=220, fg_color='lightgray', border_width=0)
        self.entry_gender.grid(row=8, column=0, pady=(0, 10))

        label_height = ctk.CTkLabel(cadastro_frame, text="ALTURA (cm)", font=('DM Sans', 10), text_color='#8f8e8e')
        label_height.grid(row=9, column=0, sticky='w', pady=(5, 2))
        self.entry_height = ctk.CTkEntry(cadastro_frame, placeholder_text="Altura (cm)", width=220, fg_color='lightgray', border_width=0)
        self.entry_height.grid(row=10, column=0, pady=(0, 10))

        label_weight = ctk.CTkLabel(cadastro_frame, text="PESO (kg)", font=('DM Sans', 10), text_color='#8f8e8e')
        label_weight.grid(row=11, column=0, sticky='w', pady=(5, 2))
        self.entry_weight = ctk.CTkEntry(cadastro_frame, placeholder_text="Peso (kg)", width=220, fg_color='lightgray', border_width=0)
        self.entry_weight.grid(row=12, column=0, pady=(0, 10))

        label_shoe_size = ctk.CTkLabel(cadastro_frame, text="TAMANHO DO CALÇADO", font=('DM Sans', 10), text_color='#8f8e8e')
        label_shoe_size.grid(row=13, column=0, sticky='w', pady=(5, 2))
        self.entry_shoe_size = ctk.CTkEntry(cadastro_frame, placeholder_text="Tamanho do Calçado", width=220, fg_color='lightgray', border_width=0)
        self.entry_shoe_size.grid(row=14, column=0, pady=(0, 10))

        label_password = ctk.CTkLabel(cadastro_frame, text="SENHA", font=('DM Sans', 10), text_color='#8f8e8e')
        label_password.grid(row=15, column=0, sticky='w', pady=(5, 2))
        self.entry_password = ctk.CTkEntry(cadastro_frame, placeholder_text="Senha", show='*', width=220, fg_color='lightgray', border_width=0)
        self.entry_password.grid(row=16, column=0, pady=(0, 10))

        label_confirm_password = ctk.CTkLabel(cadastro_frame, text="CONFIRMAR SENHA", font=('DM Sans', 10), text_color='#8f8e8e')
        label_confirm_password.grid(row=17, column=0, sticky='w', pady=(5, 2))
        self.entry_confirm_password = ctk.CTkEntry(cadastro_frame, placeholder_text="Confirmar Senha", show='*', width=220, fg_color='lightgray', border_width=0)
        self.entry_confirm_password.grid(row=18, column=0, pady=(0, 10))

        button_register = ctk.CTkButton(cadastro_frame, text="Criar Conta", font=('Poppins Bold', 13, 'bold'), fg_color='#4094a5', command=self.register_user)
        button_register.grid(row=19, column=0, pady=10)

        button_back_to_login = ctk.CTkButton(cadastro_frame, text="Voltar ao Login", font=('Poppins Bold', 13, 'bold'), fg_color='#4094a5', command=self.back_to_login)
        button_back_to_login.grid(row=20, column=0, pady=10)

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

        if not all([email, full_name, age, gender, height, weight, shoe_size, password, confirm_password]):
            messagebox.showerror("Erro", "Todos os campos são obrigatórios.")
            return

        if '@' not in email:
            messagebox.showerror("Erro", "E-mail inválido. Certifique-se de que o e-mail contém '@'.")
            return

        if password != confirm_password:
            messagebox.showerror("Erro", "As senhas não coincidem.")
            return

        if gender not in ['MALE', 'FEMALE']:
            messagebox.showerror("Erro", "Gênero inválido. Use 'MALE' ou 'FEMALE'.")
            return

        try:
            self.controller.add_user(email, full_name, int(age), gender, int(height), int(weight), int(shoe_size), password)
            messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
            self.controller.back_to_login()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao cadastrar usuário: {e}")

    def back_to_login(self):
        self.controller.back_to_login()

    def close(self):
        self.root.destroy()