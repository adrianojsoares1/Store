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
        self.categories = {"Physical": ["Computers", "Monitors", "Textbooks"],
                           "Digital": ["Gift Cards", "Steam Codes", "E-books"],
                           "Subscription": ["Classes", "Anti-virus", "Video Streaming"]}
        self.add_administrator("Adriano", "Gvr8Phc")

    def _add_user(self, name, password, acct_type):
        if acct_type == "Administrator":
            temp = Administrator(name)
        elif acct_type == "Customer":
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

    def user_login(self, username, pass_code):
        try:
            if self.login.get(username) is not None:
                new_pass = hashlib.sha512(str.encode(pass_code))
                if new_pass is self.login[username]:
                    self.current_user = self.users[new_pass]
                else:
                    raise LookupError("Password is incorrect!")
            else:
                raise LookupError("Username not found!")
        except Exception as e:
            print(str(e))

s = Store()
s.add_administrator("Nick", "password")
s.user_login("Adriano", "Gvr8Phc")
#print(s.current_user.get_username())
dicto = {"hey": "what"}

