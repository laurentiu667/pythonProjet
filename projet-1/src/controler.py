# controller.py
from model import *
from view import *

class UserController:
    def __init__(self, user_model, user_view):
        self.user_model = user_model
        self.user_view = user_view

    def set_user_name(self, name):
        self.user_model.name = name

    def set_user_age(self, age):
        self.user_model.age = age

    def display_user(self):
        self.user_view.display_user(self.user_model)

# Utilisation du MVC
if __name__ == "__main__":
    user_model = UserModel("John Doe", 25)
    user_view = UserView()
    user_controller = UserController(user_model, user_view)

    user_controller.display_user()  # Affiche les informations de l'utilisateur
    user_controller.set_user_name("Jane Doe")
    user_controller.set_user_age(30)
    user_controller.display_user()  # Affiche les nouvelles informations de l'utilisateur
