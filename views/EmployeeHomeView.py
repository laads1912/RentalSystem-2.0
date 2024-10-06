import customtkinter as ctk
from views.common.BaseLayout import create_background, create_header, initialize_window, create_title


class EmployeeHomeView:
    def __init__(self, controller):
        self.controller = controller
        self.root = initialize_window()

        self.setup_ui()

    def setup_ui(self, is_employee = False):
        background_frame = create_background(self.root)
        if not is_employee:
            create_header(background_frame)
            self.create_buttons(background_frame)
        else:
            self.create_employee_home_header(background_frame)
            create_title(background_frame, 'Rental Requests')

    def create_buttons(self, parent):
        buttons_frame = ctk.CTkFrame(parent, corner_radius=0, fg_color="white", width=400, height=200)
        buttons_frame.place(relx=0.5, rely=0.5, anchor='center')

        employee_button = ctk.CTkButton(
            buttons_frame,
            command=self.employee_button_action,
            text='EMPLOYEE',
            font=('Poppins Medium', 20, 'bold'),
            fg_color='#4094a5',
            width=200,
            height=200
        )
        employee_button.grid(row=0, column=0, padx=(0, 50))

        guest_button = ctk.CTkButton(
            buttons_frame,
            command=self.guest_button_action,
            text='GUEST',
            font=('Poppins Medium', 20, 'bold'),
            fg_color='#4094a5',
            width=200,
            height=200
        )
        guest_button.grid(row=0, column=1, padx=(50, 0))

    def create_employee_home_header(self, parent):
        header_frame = ctk.CTkFrame(parent, height=50, fg_color='#81c9d8', corner_radius=0)
        header_frame.pack(fill='x')

        header_label = ctk.CTkLabel(
            header_frame,
            text="RENTAL SYSTEM",
            font=('Poppins Medium', 18, 'bold'),
            text_color="#535353"
        )
        header_label.pack(side='left', padx=10)

        spacer_label = ctk.CTkLabel(
            header_frame,
            text="RENTAL SYSTEM",
            font=('Poppins Medium', 18, 'bold'),
            text_color="#81c9d8"
        )
        spacer_label.pack(side='right', padx=10)

        buttons_frame = ctk.CTkFrame(header_frame, fg_color='#81c9d8')
        buttons_frame.pack(side='top', pady=5)

        equipments_button = ctk.CTkButton(
            buttons_frame,
            text='',
            fg_color='#535353',
            command=self.equipments_button_action,
            width=30,
            height=30
        )
        equipments_button.grid(row=0, column=0, padx=10)

        logout_button = ctk.CTkButton(
            buttons_frame,
            text='',
            command=self.logout_button_action,
            fg_color='#535353',
            width=30,
            height=30
        )
        logout_button.grid(row=0, column=1, padx=10)

        registered_users_button = ctk.CTkButton(
            buttons_frame,
            text='',
            fg_color='#535353',
            command=self.registered_users_button_action,
            width=30,
            height=30
        )
        registered_users_button.grid(row=0, column=2, padx=10)

    def equipments_button_action(self):
        self.controller.equipments_page()

    def logout_button_action(self):
        self.controller.logout()

    def registered_users_button_action(self):
        self.controller.open_registered_users_page()

    def employee_button_action(self):
        self.setup_ui(True)

    def guest_button_action(self):
        self.controller.guest_page()

    def mainloop(self):
        self.root.mainloop()
