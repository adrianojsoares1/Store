from .User import User


class Customer(User):

    def __init__(self, username):
        self.cart = []
        self.balance = 0
        User.__init__(self, username)

    def add_to_cart(self, item):
        if len(self.cart) == 1:
            self.cart[0] = item
        else:
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
        if self.get_cart_total() > self.balance:
            raise ValueError("Not enough funds to complete transaction.")
        else:
            for i in self.cart:
                if type(i) is "Physical_Product":
                    i.buy_1()
            self.balance -= self.get_cart_total()
            self.cart = []
