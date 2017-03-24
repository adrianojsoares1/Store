from .User import User
from random import randint

class Customer(User):

    def __init__(self, username):
        self.cart = []
        self.balance = 0
        User.__init__(self, username)

    def add_to_cart(self, item):
        self.cart.append(item)

    def delete_from_cart(self, item):
        self.cart.remove(item)

    def add_to_balance(self, amt):
        self.balance += amt

    def retract_funds(self, amt):
        self.balance -= amt

    def get_cart(self):
        return self.cart

    def get_balance(self):
        return self.balance

    def get_cart_total(self):
        sm = 0
        for i in self.cart:
            sm += i.get_price()
        return sm

    def purchase(self):
        logs = []
        max_name = 20
        tmp = ""
        try:
            if self.get_cart_total() > self.balance:
                raise ValueError("Not enough funds to complete transaction.")
            else:
                for i in self.cart:
                    if type(i) is "Physical_Product":
                        i.buy_1()

                    tmp += i.get_name()
                    for j in range(0, (max_name - len(i.get_name()))):
                        tmp += " "
                    tmp += "| " + str(randint(1000,9999)) + "               |" + str(i.get_price())
                    logs.append(tmp)
                    tmp = ""
                self.balance -= self.get_cart_total()
                self.cart = []
                return logs
        except ValueError as e:
            print(str(e))
