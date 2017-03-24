from Web_Store.Digital_Product import Digital_Product
from Web_Store.Physical_Product import Physical_Product
from Web_Store.Subscription_Product import Subscription_Product
import hashlib
from Web_Store.Customer import *
from Web_Store.Administrator import *


class Store:

    def __init__(self):

        self.login = {}
        self.users = {}
        self.current_user = None
        self.categories = {"Physical": {"Computers": [Physical_Product()],
                                        "Monitors": [],
                                        "Textbooks": []},
                           "Digital": {"Gift Cards": [],
                                       "Steam Codes": [],
                                       "E-books": []},
                           "Subscription": {"Classes": [],
                                            "Anti-virus": [],
                                            "Video Streaming": []}
                           }

        self.purchase_log = {}

    def get_categories(self):
        return self.categories

    def _add_user(self, name, password, acct_type):
        if acct_type == "Administrator":
            temp = Administrator(name)
        elif acct_type == "Customer":
            temp = Customer(name)
        else:
            raise ValueError("Not a valid type!")

        # password = str.encode(password)
        # hashed_pass = hashlib.sha512(password)

        self.login[name] = password
        self.users[password] = temp

    def add_administrator(self, name, password):
        self._add_user(name, password, "Administrator")

    def add_customer(self, name, password):
        self._add_user(name, password, "Customer")

    def change_user_password(self, new_pass):
        if self.current_user is not None:
            # temp_pass = hashlib.sha512(str.encode(new_pass))

            del self.users[self.login[self.current_user.get_username()]]  # because key is immutable

            self.login[self.current_user.get_username()] = new_pass  # Set new login pass

            self.users[new_pass] = self.current_user  # add new dict entry
        else:
            raise ValueError("'None' is not a valid user!")

    def user_login(self, username, pass_code):
        try:
            if self.login.get(username) is not None:
                # new_pass = hashlib.sha512(str.encode(pass_code))
                if pass_code == self.login[username]:
                    self.current_user = self.users[pass_code]
                else:
                    raise LookupError("Password is incorrect!\n")
            else:
                raise LookupError("Username not found!\n")
        except LookupError as e:
            return str(e)
        return "Login Successful"

    def user_logout(self):
        self.current_user = None

    def add_category(self, master_cat, new_sub_cat):
        try:
            self.check_permission()
            if self.categories.get(master_cat) is not None:
                self.categories[master_cat][new_sub_cat] = []
            else:
                raise FileExistsError("Entry already exists or is not valid.")
        except BaseException as e:
            print(str(e))

    def add_product(self, product):
        try:
            self.check_permission()
            key = ""
            if type(product) is Physical_Product:
                key = "Physical"
            elif type(product) is Digital_Product:
                key = "Digital"
            elif type(product) is Subscription_Product:
                key = "Subscription"
            self.categories[key][product.get_category()].append(product)
        except PermissionError as e:
            print(e)

    def check_permission(self):
        if type(self.current_user) is not Administrator:
            raise PermissionError("Only administrators can modify this field.")

    def set_product_price(self, product, new_price):
        try:
            self.check_permission()
            product.set_price(new_price)
        except PermissionError as e:
            print(e)

    def restock(self, product, new_quantity):
        try:
            self.check_permission()
            print("Original Quantity:", product.get_quantity(), "|New Quantity:", new_quantity, "|Final:",
                  product.get_quantity() + new_quantity)
            product.set_quantity((product.get_quantity() + new_quantity))
        except PermissionError as e:
            print(e)

'''
s = Store()
s.add_administrator("Adriano", "Gvr8Phc")
s.user_login("Adriano", "Gvr8Phc")
print(s.current_user.get_username())
print(type(s.current_user) == Administrator)
'''
