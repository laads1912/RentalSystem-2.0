from controllers.RegisteredUsersController import RegisteredUsersController
from views.GuestHomeView import GuestHomeView

class GuestHomeController:
    def __init__(self, login_controller):
        self.login_controller = login_controller
        self.registered_users_controller = RegisteredUsersController(self)  

    def open_edit_user(self, email):
        self.registered_users_controller.open_user_edit_page(email)
        self.view.root.withdraw()

    def open_home_page(self, email):
        self.view = GuestHomeView(self, email)
        self.view.root.mainloop(email)

    def log_out(self):
        self.view.root.withdraw()
        self.login_controller.view.root.deiconify()
