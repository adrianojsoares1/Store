#from .Product import Product
#from .Digital_Product import Digital_Product
#from .Physical_Product import Physical_Product
#from .Subscription_Product import Subscription_Product
import hashlib
from Web_Store.User import *
from Web_Store.Customer import *
from Web_Store.Administrator import *


class Store:

    def __init__(self):

        self.login = {}
        self.users = {}
        self.current_user = None
        self.add_administrator("Adriano", "Gvr8Phc")


    def _add_user(self, name, password, type):
        if type == "Administrator":
            temp = Administrator(name)
        elif type == "Customer":
            temp = Customer(name)
        else:
            raise ValueError("Not a valid type!")

        password = str.encode(password)
        hashed_pass = hashlib.sha512(password)

        self.login[name] = hashed_pass
        self.users[hashed_pass] = temp

    def add_administrator(self, name, password):
        self._add_user(name, password, "Administrator")

    def add_customer(self, name, password):
        self._add_user(name, password, "Customer")

    def change_user_password(self, new_pass):
        if self.current_user is not None:
            temp_pass = hashlib.sha512(str.encode(new_pass))

            del self.users[self.login[self.current_user.get_username()]]  # because key is immutable

            self.login[self.current_user.get_username()] = temp_pass  # Set new login pass

            self.users[temp_pass] = self.current_user  # add new dict entry
        else:
            raise ValueError("'None' is not a valid user!")


s = Store()
s.add_administrator("Nick", "password")
print(s.login["Adriano"])
