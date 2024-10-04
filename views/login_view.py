import customtkinter as ctk
from tkinter import messagebox

root = ctk.CTk()
root.title("RENTAL SYSTEM")
root.geometry("800x600")

background_frame = ctk.CTkFrame(root, corner_radius=0, fg_color='white')
background_frame.place(relwidth=1, relheight=1)

header_frame = ctk.CTkFrame(background_frame, height=50, fg_color='#81c9d8', corner_radius=0)
header_frame.pack(fill='x')

header_label = ctk.CTkLabel(header_frame, text="RENTAL SYSTEM", font=('Poppins Medium', 18, 'bold'), text_color="#535353")
header_label.pack(side='left', padx=10)

login_frame = ctk.CTkFrame(background_frame, corner_radius=0, fg_color="white")
login_frame.pack(pady=20)
login_frame.place(relx=0.5, rely=0.5, anchor='center')

login_label = ctk.CTkLabel(login_frame, text="Login", font=('Poppins Medium', 30, 'bold'), text_color='#8f8e8e')
login_label.grid(row=0, column=0, columnspan=2, pady=10)

email_label = ctk.CTkLabel(login_frame, text="EMAIL", font=('DM Sans', 10), text_color='#8f8e8e')
email_label.grid(row=1, column=0, sticky='w', pady=(5, 2))

email_entry = ctk.CTkEntry(login_frame, width=220, fg_color='lightgray', border_width=0)
email_entry.grid(row=2, column=0, pady=(0, 10))

password_label = ctk.CTkLabel(login_frame, text="PASSWORD", font=('DM Sans', 10), text_color='#8f8e8e')
password_label.grid(row=3, column=0, sticky='w', pady=(5, 2))

password_entry = ctk.CTkEntry(login_frame, show='*', width=220, fg_color='lightgray', border_width=0)
password_entry.grid(row=4, column=0, pady=(0, 10))

create_account_label = ctk.CTkLabel(login_frame, text="Create new account", font=('Telegraf', 10, 'bold'), text_color="#4094a5")
create_account_label.grid(row=5, column=0, pady=10)
create_account_label.bind("<Button-1>")

sign_in_button = ctk.CTkButton(login_frame, text="Sign In", font=('Poppins Bols', 13, 'bold'), fg_color='#4094a5')
sign_in_button.grid(row=6, column=0, pady=10)

root.mainloop()
