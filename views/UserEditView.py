import customtkinter as ctk
from tkinter import messagebox

class UserEditView:
    def __init__(self, controller, user):
        self.controller = controller
        self.user = user
        self.root = ctk.CTk()
        self.root.title("RENTAL SYSTEM - Edit Account")
        self.root.geometry("1000x700")

        background_frame = ctk.CTkFrame(self.root, corner_radius=0, fg_color='white')
        background_frame.place(relwidth=1, relheight=1)

        header_frame = ctk.CTkFrame(background_frame, height=50, fg_color='#81c9d8', corner_radius=0)
        header_frame.pack(fill='x')

        header_label = ctk.CTkLabel(header_frame, text="RENTAL SYSTEM", font=('Poppins Medium', 18, 'bold'), text_color="#535353")
        header_label.pack(side='left', padx=10)

        edit_frame = ctk.CTkFrame(background_frame, corner_radius=10, fg_color="white")
        edit_frame.pack(pady=20)
        edit_frame.place(relx=0.5, rely=0.5, anchor='center')

        edit_label = ctk.CTkLabel(edit_frame, text="Editar Perfil", font=('Poppins Medium', 30, 'bold'), text_color='#8f8e8e')
        edit_label.grid(row=0, column=0, columnspan=2, pady=10)

        label_email = ctk.CTkLabel(edit_frame, text="EMAIL", font=('DM Sans', 10), text_color='#8f8e8e')
        label_email.grid(row=1, column=0, sticky='w', pady=(5, 2))
        self.entry_email = ctk.CTkEntry(edit_frame, placeholder_text="Email", width=220, fg_color='lightgray', border_width=0)
        self.entry_email.grid(row=2, column=0, pady=(0, 10))
        self.entry_email.insert(0, self.user['email'])

        label_name = ctk.CTkLabel(edit_frame, text="NOME COMPLETO", font=('DM Sans', 10), text_color='#8f8e8e')
        label_name.grid(row=3, column=0, sticky='w', pady=(5, 2))
        self.entry_name = ctk.CTkEntry(edit_frame, placeholder_text="Nome Completo", width=220, fg_color='lightgray', border_width=0)
        self.entry_name.grid(row=4, column=0, pady=(0, 10))
        self.entry_name.insert(0, self.user['full_name'])

        label_age = ctk.CTkLabel(edit_frame, text="IDADE", font=('DM Sans', 10), text_color='#8f8e8e')
        label_age.grid(row=5, column=0, sticky='w', pady=(5, 2))
        self.entry_age = ctk.CTkEntry(edit_frame, placeholder_text="Idade", width=220, fg_color='lightgray', border_width=0)
        self.entry_age.grid(row=6, column=0, pady=(0, 10))
        self.entry_age.insert(0, self.user['age'])

        label_gender = ctk.CTkLabel(edit_frame, text="GÊNERO", font=('DM Sans', 10), text_color='#8f8e8e')
        label_gender.grid(row=7, column=0, sticky='w', pady=(5, 2))
        self.entry_gender = ctk.CTkEntry(edit_frame, placeholder_text="Gênero (MALE/FEMALE)", width=220, fg_color='lightgray', border_width=0)
        self.entry_gender.grid(row=8, column=0, pady=(0, 10))
        self.entry_gender.insert(0, self.user['gender'])

        label_height = ctk.CTkLabel(edit_frame, text="ALTURA (cm)", font=('DM Sans', 10), text_color='#8f8e8e')
        label_height.grid(row=9, column=0, sticky='w', pady=(5, 2))
        self.entry_height = ctk.CTkEntry(edit_frame, placeholder_text="Altura (cm)", width=220, fg_color='lightgray', border_width=0)
        self.entry_height.grid(row=10, column=0, pady=(0, 10))
        self.entry_height.insert(0, self.user['height'])

        label_weight = ctk.CTkLabel(edit_frame, text="PESO (kg)", font=('DM Sans', 10), text_color='#8f8e8e')
        label_weight.grid(row=11, column=0, sticky='w', pady=(5, 2))
        self.entry_weight = ctk.CTkEntry(edit_frame, placeholder_text="Peso (kg)", width=220, fg_color='lightgray', border_width=0)
        self.entry_weight.grid(row=12, column=0, pady=(0, 10))
        self.entry_weight.insert(0, self.user['weight'])

        label_shoe_size = ctk.CTkLabel(edit_frame, text="TAMANHO DO CALÇADO", font=('DM Sans', 10), text_color='#8f8e8e')
        label_shoe_size.grid(row=13, column=0, sticky='w', pady=(5, 2))
        self.entry_shoe_size = ctk.CTkEntry(edit_frame, placeholder_text="Tamanho do Calçado", width=220, fg_color='lightgray', border_width=0)
        self.entry_shoe_size.grid(row=14, column=0, pady=(0, 10))
        self.entry_shoe_size.insert(0, self.user['shoe_size'])

        label_password = ctk.CTkLabel(edit_frame, text="NOVA SENHA", font=('DM Sans', 10), text_color='#8f8e8e')
        label_password.grid(row=15, column=0, sticky='w', pady=(5, 2))
        self.entry_password = ctk.CTkEntry(edit_frame, placeholder_text="Nova Senha", show='*', width=220, fg_color='lightgray', border_width=0)
        self.entry_password.grid(row=16, column=0, pady=(0, 10))

        label_confirm_password = ctk.CTkLabel(edit_frame, text="CONFIRMAR SENHA", font=('DM Sans', 10), text_color='#8f8e8e')
        label_confirm_password.grid(row=17, column=0, sticky='w', pady=(5, 2))
        self.entry_confirm_password = ctk.CTkEntry(edit_frame, placeholder_text="Confirmar Senha", show='*', width=220, fg_color='lightgray', border_width=0)
        self.entry_confirm_password.grid(row=18, column=0, pady=(0, 10))

        button_update = ctk.CTkButton(edit_frame, text="Atualizar", font=('Poppins Bold', 13, 'bold'), fg_color='#4094a5', command=self.update_user)
        button_update.grid(row=19, column=0, pady=10)

        button_back = ctk.CTkButton(edit_frame, text="Cancelar", font=('Poppins Bold', 13, 'bold'), fg_color='#4094a5', command=self.back_to_login)
        button_back.grid(row=20, column=0, pady=10)

    def update_user(self):
        email = self.entry_email.get()
        full_name = self.entry_name.get()
        age = self.entry_age.get()
        gender = self.entry_gender.get().upper()
        height = self.entry_height.get()
        weight = self.entry_weight.get()
        shoe_size = self.entry_shoe_size.get()
        password = self.entry_password.get()
        confirm_password = self.entry_confirm_password.get()

        if not all([email, full_name, age, gender, height, weight, shoe_size]):
            messagebox.showerror("Erro", "Todos os campos são obrigatórios, exceto senha.")
            return

        if '@' not in email:
            messagebox.showerror("Erro", "E-mail inválido. Certifique-se de que o e-mail contém '@'.")
            return

        if gender not in ['MALE', 'FEMALE']:
            messagebox.showerror("Erro", "Gênero inválido. Use 'MALE' ou 'FEMALE'.")
            return

        if password or confirm_password:
            if password != confirm_password:
                messagebox.showerror("Erro", "As senhas não coincidem.")
                return

        try:
            self.controller.update_user(email, full_name, int(age), gender, int(height), int(weight), int(shoe_size), password)
            messagebox.showinfo("Sucesso", "Usuário atualizado com sucesso!")
            self.controller.back_to_login()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao atualizar usuário: {e}")

    def back_to_login(self):   
        self.controller.back_to_login()

    def close(self):
        self.root.destroy()
