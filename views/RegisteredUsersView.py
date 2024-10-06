import customtkinter as ctk
from tkinter import messagebox

class RegisteredUsersView:
    def __init__(self, controller):
        self.controller = controller
        self.root = self.initialize_window()

        self.setup_ui()

    def initialize_window(self):
        root = ctk.CTk()
        root.title("RENTAL SYSTEM")
        root.geometry("1000x700")
        return root

    def setup_ui(self):
        background_frame = self.create_background()
        self.create_header(background_frame)
        self.create_title(background_frame)
        self.create_users_cards(background_frame)

    def create_background(self):
        background_frame = ctk.CTkFrame(self.root, corner_radius=0, fg_color='white')
        background_frame.place(relwidth=1, relheight=1)
        return background_frame

    def create_header(self, parent):
        header_frame = ctk.CTkFrame(parent, height=50, fg_color='#81c9d8', corner_radius=0)
        header_frame.pack(fill='x')

        header_label = ctk.CTkLabel(
            header_frame,
            text="RENTAL SYSTEM",
            font=('Poppins Medium', 18, 'bold'),
            text_color="#535353"
        )
        header_label.pack(side='left', padx=10)

    def create_title(self, parent):
        title_frame = ctk.CTkFrame(parent, corner_radius=0, fg_color="white", width=400)
        title_frame.pack(pady=20)

        title_label = ctk.CTkLabel(
            title_frame,
            text="Registered Users",
            font=('Poppins Medium', 50, 'bold'),
            text_color='#8f8e8e'
        )
        title_label.grid(row=0, column=0, pady=10)

    def create_users_cards(self, parent):
        users_frame = ctk.CTkScrollableFrame(parent, corner_radius=0, fg_color="white", width=1000)
        users_frame.pack(fill='y', expand=True)

        users = ["John Doe", "Jane Smith", "Alex Johnson", "Chris Lee", "Emma Stone", "Will Turner", "Bruce Wayne"]

        num_columns = 4

        users_frame.grid_columnconfigure(tuple(range(num_columns)), weight=1)

        for index, user in enumerate(users):
            row = index // num_columns
            col = index % num_columns
            self.create_card(users_frame, user, row, col)

    def create_card(self, parent, user, row, col):
        card_frame = ctk.CTkFrame(parent, corner_radius=10, fg_color="lightgray", width=200, height=150)
        card_frame.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

        card_frame.bind("<Button-1>", lambda event, u=user: self.on_card_click(u))

        card_frame.grid_columnconfigure(0, weight=1)

        name_label = ctk.CTkLabel(
            card_frame,
            text=user,
            bg_color='#81c9d8',
            font=('Poppins Medium', 20, 'bold'),
            text_color='#8f8e8e'
        )
        name_label.grid(row=0, column=0, sticky="nsew")

        gender_label = ctk.CTkLabel(
            card_frame,
            text="Gender: teste",
            font=('Poppins Medium', 15),
            text_color='#8f8e8e'
        )
        gender_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)

        age_label = ctk.CTkLabel(
            card_frame,
            text="Age: teste",
            font=('Poppins Medium', 15),
            text_color='#8f8e8e'
        )
        age_label.grid(row=2, column=0, sticky="w", padx=10, pady=5)

    def on_card_click(self, user):
        messagebox.showinfo("Card Clicked", f"You clicked on {user}")

    def mainloop(self):
        self.root.mainloop()
