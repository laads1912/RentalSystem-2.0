import customtkinter as ctk
from tkinter import messagebox

class LoginView:
    def __init__(self, controller):
        self.controller = controller
        self.root = ctk.CTk()
        self.root.title("RENTAL SYSTEM - Login")
        self.root.geometry("1000x700")

        background_frame = ctk.CTkFrame(self.root, corner_radius=0, fg_color='white')
        background_frame.place(relwidth=1, relheight=1)

        header_frame = ctk.CTkFrame(background_frame, height=50, fg_color='#81c9d8', corner_radius=0)
        header_frame.pack(fill='x')

        header_label = ctk.CTkLabel(header_frame, text="RENTAL SYSTEM", font=('Poppins Medium', 18, 'bold'), text_color="#535353")
        header_label.pack(side='left', padx=10)

        self.login_frame = ctk.CTkFrame(background_frame, corner_radius=0, fg_color="white")
        self.login_frame.pack(pady=20)
        self.login_frame.place(relx=0.5, rely=0.5, anchor='center')

        login_label = ctk.CTkLabel(self.login_frame, text="Login", font=('Poppins Medium', 30, 'bold'), text_color='#8f8e8e')
        login_label.grid(row=0, column=0, columnspan=2, pady=10)

        email_label = ctk.CTkLabel(self.login_frame, text="EMAIL", font=('DM Sans', 10), text_color='#8f8e8e')
        email_label.grid(row=1, column=0, sticky='w', pady=(5, 2))

        self.email_entry = ctk.CTkEntry(self.login_frame, width=220, fg_color='lightgray', border_width=0, text_color='#4a4a4a')
        self.email_entry.grid(row=2, column=0, pady=(0, 10))

        password_label = ctk.CTkLabel(self.login_frame, text="PASSWORD", font=('DM Sans', 10), text_color='#8f8e8e')
        password_label.grid(row=3, column=0, sticky='w', pady=(5, 2))

        self.password_entry = ctk.CTkEntry(self.login_frame, show='*', width=220, fg_color='lightgray', border_width=0, text_color='#4a4a4a')
        self.password_entry.grid(row=4, column=0, pady=(0, 10))

        create_account_label = ctk.CTkLabel(self.login_frame, text="Create new account", font=('Telegraf', 10, 'bold'), text_color="#4094a5")
        create_account_label.grid(row=5, column=0, pady=10)
        create_account_label.bind("<Button-1>", self.open_registration)

        sign_in_button = ctk.CTkButton(self.login_frame, text="Sign In", font=('Poppins Bols', 13, 'bold'), fg_color='#4094a5', command=self.login)
        sign_in_button.grid(row=6, column=0, pady=10)

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        self.controller.handle_login(email, password)

    def open_registration(self, event):
        self.controller.handle_open_registration()

    def show_message(self, title, message):
        messagebox.showinfo(title, message)

    def mainloop(self):
        self.root.mainloop()