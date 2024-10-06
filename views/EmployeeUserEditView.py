import customtkinter as ctk
from tkinter import messagebox

from models.enums import GenderEnum
from views.common.BaseLayout import create_background, initialize_window, create_header


class EmployeeUserEditView:
    def __init__(self, controller):
        self.controller = controller
        self.root = initialize_window()

        self.full_name_entry = ''
        self.email_entry = ''
        self.password_entry = ''
        self.password_confirmation_entry = ''
        self.gender_entry = ''
        self.us_shoe_size_entry = ''
        self.age_entry = ''
        self.is_employee_entry = ''
        self.weight_entry = ''
        self.height_entry = ''

        self.setup_ui()

    def setup_ui(self):
        background_frame = create_background(self.root)
        create_header(background_frame)
        self.create_form_title(background_frame)
        self.create_edit_user_form(background_frame)

    def create_form_title(self, parent):
        title_frame = ctk.CTkFrame(parent, corner_radius=0, fg_color="white", width=400)
        title_frame.pack(pady=20)

        title_frame.grid_columnconfigure(0, weight=1)
        title_frame.grid_columnconfigure(1, weight=0)
        title_frame.grid_columnconfigure(2, weight=1)

        trash_button = ctk.CTkButton(
            title_frame,
            command=self.trash_button_action,
            text='',
            fg_color='#4094a5',
            width=20,
            height=20
        )
        trash_button.grid(row=0, column=0, padx=(0, 10))

        edit_label = ctk.CTkLabel(
            title_frame,
            text="Edit User Information",
            font=('Poppins Medium', 50, 'bold'),
            text_color='#8f8e8e'
        )
        edit_label.grid(row=0, column=1, pady=10)

        return_button = ctk.CTkButton(
            title_frame,
            command=self.return_button_action,
            text='',
            fg_color='#4094a5',
            width=20,
            height=20
        )
        return_button.grid(row=0, column=2, padx=(10, 0))

    def create_edit_user_form(self, parent):
        form_frame = ctk.CTkScrollableFrame(parent, corner_radius=0, fg_color="white", width=400)
        form_frame.pack(fill='y', expand=True)

        self.full_name_entry = self.create_form_field(form_frame, "FULL NAME", 2)
        self.email_entry = self.create_form_field(form_frame, "EMAIL", 4)
        self.password_entry = self.create_form_field(form_frame, "PASSWORD", 6, {"show": '*'})
        self.password_confirmation_entry = self.create_form_field(form_frame, "PASSWORD CONFIRMATION", 8, {"show": '*'})
        self.gender_entry = self.create_gender_select(form_frame, "GENDER", 10)
        self.us_shoe_size_entry = self.create_form_field(form_frame, "US SHOE SIZE", 12)
        self.age_entry = self.create_form_field(form_frame, "AGE", 14)
        self.is_employee_entry = self.create_radio_buttons(form_frame, "EMPLOYEE", 16)
        self.weight_entry = self.create_form_field(form_frame, "WEIGHT (KG)", 18)
        self.height_entry = self.create_form_field(form_frame, "HEIGHT (CM)", 20)

        self.create_buttons(form_frame)

    def create_form_field(self, parent, label_text, row, entry_options=None):
        parent.grid_columnconfigure(0, minsize=120)
        parent.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(parent, text=label_text, text_color='#8f8e8e').grid(
            row=row, column=0, columnspan=2, sticky='w', padx=10, pady=(5, 2)
        )

        entry_options = entry_options or {}
        entry = ctk.CTkEntry(
            parent,
            width=220,
            fg_color='lightgray',
            border_width=0,
            text_color='#4a4a4a',
            **entry_options
        )
        entry.grid(row=row + 1, column=0, columnspan=2, padx=10, pady=(0, 10), sticky='nsew')

        return entry

    def create_gender_select(self, parent, label_text, row, default_value=GenderEnum.MALE.value):
        gender_options = [GenderEnum.MALE.value, GenderEnum.FEMALE.value]
        entry = ctk.StringVar(value=default_value)

        ctk.CTkLabel(parent, text=label_text, text_color='#8f8e8e').grid(
            row=row, column=0, columnspan=2, padx=10, pady=(5, 2), sticky='w'
        )

        gender_select = ctk.CTkOptionMenu(
            parent,
            variable=entry,
            fg_color='lightgray',
            button_color='lightgray',
            button_hover_color='gray',
            dropdown_fg_color='lightgray',
            dropdown_text_color='#4a4a4a',
            dropdown_hover_color='gray',
            text_color='#4a4a4a',
            values=gender_options
        )
        gender_select.grid(row=row + 1, column=0, columnspan=2, padx=10, pady=(0, 10), sticky='nsew')

        return entry

    def create_radio_buttons(self, parent, label_text, row, default_value='No'):
        parent.grid_columnconfigure(0, minsize=120)
        parent.grid_columnconfigure(1, weight=1)

        employee_label = ctk.CTkLabel(parent, text=label_text, text_color='#8f8e8e')
        employee_label.grid(row=row, column=0, columnspan=2, padx=10, pady=(0, 10), sticky='w')

        entry = ctk.StringVar(value=default_value)

        ctk.CTkRadioButton(parent, text='Yes', variable=entry, value='Yes', text_color='#8f8e8e').grid(
            row=row + 1, column=0, padx=(10, 0), pady=(0, 5), sticky='w'
        )
        ctk.CTkRadioButton(parent, text='No', variable=entry, value='No', text_color='#8f8e8e').grid(
            row=row + 1, column=1, padx=(0, 10), pady=(0, 5), sticky='w'
        )

        return entry

    def trash_button_action(self):
        messagebox.showinfo("Info", "Trash button clicked")

    def return_button_action(self):
        messagebox.showinfo("Info", "Return button clicked")

    def create_buttons(self, parent):
        buttons = [
            ("Rental History", self.rental_historic),
            ("Save", self.save),
            ("Working History", self.working_historic)
        ]
        for i, (text, command) in enumerate(buttons):
            ctk.CTkButton(
                parent,
                text=text,
                font=('Poppins Bold', 13, 'bold'),
                fg_color='#81c9d8',
                command=command
            ).grid(row=22 + i, column=0, columnspan=2, pady=10)

    def rental_historic(self):
        messagebox.showinfo("Info", "Rental History clicked")

    def save(self):
        form_data = {
            "Full Name": self.full_name_entry.get(),
            "Email": self.email_entry.get(),
            "Password": self.password_entry.get(),
            "Password Confirmation": self.password_confirmation_entry.get(),
            "Gender": self.gender_entry.get(),
            "US Shoe Size": self.us_shoe_size_entry.get(),
            "Age": self.age_entry.get(),
            "Is Employee": self.is_employee_entry.get(),
            "Weight": self.weight_entry.get(),
            "Height": self.height_entry.get(),
        }

        messagebox.showinfo("Saved Values", "\n".join(f"{key}: {value}" for key, value in form_data.items()))

    def working_historic(self):
        messagebox.showinfo("Info", "Working History clicked")

    def mainloop(self):
        self.root.mainloop()
