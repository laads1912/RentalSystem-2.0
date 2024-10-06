import customtkinter as ctk

class HomeView:
    def __init__(self, controller, email):
        self.email = email
        self.controller = controller
        self.root = ctk.CTk()
        self.root.title("RENTAL SYSTEM - Home")
        self.root.geometry("1000x700")

        background_frame = ctk.CTkFrame(self.root, corner_radius=0, fg_color='white')
        background_frame.place(relwidth=1, relheight=1)

        header_frame = ctk.CTkFrame(background_frame, height=50, fg_color='#81c9d8', corner_radius=0)
        header_frame.pack(fill='x')

        header_label = ctk.CTkLabel(header_frame, text="RENTAL SYSTEM", font=('Poppins Medium', 18, 'bold'), text_color="#535353")
        header_label.pack(side='left', padx=10)

        account_info_frame = ctk.CTkFrame(background_frame, corner_radius=10, fg_color="white")
        account_info_frame.pack(pady=20)
        account_info_frame.place(relx=0.5, rely=0.5, anchor='center')

        account_info_button = ctk.CTkButton(account_info_frame, text="ACCOUNT INFORMATION", font=('Poppins Bold', 16, 'bold'), 
                                            fg_color='#4094a5', height=50, width=300, corner_radius=10, 
                                            command=self.open_account_information)
        account_info_button.grid(row=0, column=0, padx=10, pady=20)
        self.root.mainloop()

    def open_account_information(self):
        self.close()
        self.controller.open_edit_user(self.email)

    def close(self):
        self.root.destroy()
