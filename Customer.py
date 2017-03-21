from .User import User


class Customer(User):

    def __init__(self):
        self.cart = [None]
        self.balance = 0
        User.__init__(self)

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

    def purchase(self):
        cart_total = 0
        for i in self.cart:
            cart_total += i.get_price()

        if cart_total > self.balance:
            raise ValueError("Not enough funds to complete transaction.")
        else:
            self.balance -= cart_total
