from Web_Store.Digital_Product import Digital_Product
from Web_Store.Physical_Product import Physical_Product
from Web_Store.Subscription_Product import Subscription_Product
import hashlib
from Web_Store.Customer import *
from Web_Store.Administrator import *
import datetime


class Store:

    def __init__(self):

        self.login = {}
        self.users = {}
        self.current_user = None
        self.categories = {"Physical": {"Computers": [],
                                        "Monitors": [],
                                        "Textbooks": []},
                           "Digital": {"Gift Cards": [],
                                       "Steam Codes": [],
                                       "E-books": []},
                           "Subscription": {"Classes": [],
                                            "Anti-virus": [],
                                            "Video Streaming": []}
                           }

        self.purchase_log = ["Timestamp                   Product Name          Confirmation Code    Price"]
        self.product_log = ["Category             Product Name                               Product Type          "
                            "                                                        Items left"]
        self.users_log = ["Recent Activity:"]

    def get_categories(self):
        return self.categories

    def get_purchases(self):
        return self.purchase_log

    def get_activity(self):
        return self.users_log

    def get_products(self):
        temp = []
        string = ""
        for i in self.categories:
            for j in self.categories[i]:
                for k in self.categories[i][j]:
                    # all this for consistent formatting :'(
                    string += k.get_category()
                    for l in range(0, (20 - len(k.get_category()))):
                        string += " "
                    string += "|  " + k.get_name()
                    for l in range(0, (40 - len(k.get_name()))):
                        string += " "
                    string += "|  " + str(type(k))
                    for l in range(0, (75- len(str(type(k))))):
                        string += " "
                    if type(k) is not Physical_Product:
                        string += "| ∞"
                    else:
                        string += "| " + str(k.get_quantity())
                    temp.insert(0,string)
                    string = ""
        self.product_log += temp
        return self.product_log

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

            now = datetime.datetime.now()
            self.users_log.insert(1, self.current_user.get_username() + " has changed their password at " + str(now))
        else:
            raise ValueError("'None' is not a valid user!")

    def is_logged_in(self):
        return self.current_user is not None

    def user_login(self, username, pass_code):
        if self.is_logged_in():
            return "Login Successful"
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
        now = datetime.datetime.now()
        self.users_log.insert(1, self.current_user.get_username() + " has logged in at " + str(now))
        return "Login Successful"

    def user_logout(self):
        now = datetime.datetime.now()
        self.users_log.insert(1, self.current_user.get_username() + " has logged out at " + str(now))
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
            print("Original Quantity:", product.get_quantity(), "| Added Quantity:", new_quantity, "| Final:",
                  product.get_quantity() + new_quantity)
            product.set_quantity((product.get_quantity() + new_quantity))
        except PermissionError as e:
            print(e)

    def user_purchase(self):
        items_bought = 0
        try:
            if type(self.current_user) is Customer:
                stamp = datetime.datetime.now()
                purchaser = self.current_user.purchase()
                for i in purchaser:
                    self.purchase_log.insert(1, str(stamp) + " | " + i)
                    items_bought += 1
                now = datetime.datetime.now()
                self.users_log.insert(1, self.current_user.get_username() + " has purchased " +
                                      str(items_bought) + " items at " + str(now))
            else:
                raise PermissionError("Only customers can make a purchase.")
        except PermissionError as e:
            print(e)
