import customtkinter as ctk
from tkinter import messagebox
from views.user_view import App as CadastroApp  # Importando a tela de cadastro

class LoginApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configurações principais da janela
        self.title("RENTAL SYSTEM")
        self.geometry("800x600")

        # Fundo branco
        background_frame = ctk.CTkFrame(self, corner_radius=0, fg_color='white')
        background_frame.place(relwidth=1, relheight=1)

        # Header
        header_frame = ctk.CTkFrame(background_frame, height=50, fg_color='#81c9d8', corner_radius=0)
        header_frame.pack(fill='x')
        header_label = ctk.CTkLabel(header_frame, text="RENTAL SYSTEM", font=('Poppins Medium', 18, 'bold'), text_color="#535353")
        header_label.pack(side='left', padx=10)

        # Frame de Login
        login_frame = ctk.CTkFrame(background_frame, corner_radius=10, fg_color="white")
        login_frame.place(relx=0.5, rely=0.5, anchor='center')

        # Título do Login
        login_label = ctk.CTkLabel(login_frame, text="Login", font=('Poppins Medium', 30, 'bold'), text_color='#8f8e8e')
        login_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Campo de e-mail
        email_label = ctk.CTkLabel(login_frame, text="EMAIL", font=('DM Sans', 10), text_color='#8f8e8e')
        email_label.grid(row=1, column=0, sticky='w', pady=(5, 2))

        email_entry = ctk.CTkEntry(login_frame, width=300, fg_color='lightgray', border_width=0, height=35)
        email_entry.grid(row=2, column=0, pady=(0, 10))

        # Campo de senha
        password_label = ctk.CTkLabel(login_frame, text="PASSWORD", font=('DM Sans', 10), text_color='#8f8e8e')
        password_label.grid(row=3, column=0, sticky='w', pady=(5, 2))

        password_entry = ctk.CTkEntry(login_frame, show='*', width=300, fg_color='lightgray', border_width=0, height=35)
        password_entry.grid(row=4, column=0, pady=(0, 10))

        # Link para criar uma nova conta
        create_account_label = ctk.CTkLabel(login_frame, text="Create new account", font=('Telegraf', 10, 'bold'), text_color="#4094a5", cursor="hand2")
        create_account_label.grid(row=5, column=0, pady=10)
        create_account_label.bind("<Button-1>", self.open_register)  # Vincula o clique ao método de abrir cadastro

        # Botão de login
        sign_in_button = ctk.CTkButton(login_frame, text="Sign In", font=('Poppins Bold', 13, 'bold'), fg_color='#4094a5', width=150, height=40)
        sign_in_button.grid(row=6, column=0, pady=20)

        self.cadastro_app = None  # Inicialmente, a tela de cadastro está fechada

    def open_register(self, event):
        self.withdraw()  # Esconde a janela de login
        if self.cadastro_app is None or not self.cadastro_app.winfo_exists():
            self.cadastro_app = CadastroApp(self.show_login)
        else:
            self.cadastro_app.deiconify()  # Reexibe a janela de cadastro se já foi aberta
        self.cadastro_app.mainloop()

    def show_login(self):
        if self.cadastro_app is not None:
            self.cadastro_app.withdraw()  # Esconde a janela de cadastro
        self.deiconify()  # Reexibe a janela de login

if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()
