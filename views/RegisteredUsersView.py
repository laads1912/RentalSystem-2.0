import customtkinter as ctk

from views.common.BaseLayout import initialize_window, create_header, create_background, create_title


class RegisteredUsersView:
    def __init__(self, controller):
        self.controller = controller
        self.root = initialize_window()

        self.setup_ui()

    def setup_ui(self):
        background_frame = create_background(self.root)
        create_header(background_frame)
        create_title(background_frame, 'Registered Users')
        self.create_users_cards(background_frame)

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

    def on_card_click(self, email):
        self.controller.open_employee_user_edit_page(email)

    def mainloop(self):
        self.root.mainloop()
