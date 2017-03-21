from .User import User


class Administrator(User):

    def __init__(self, username):
        User.__init__(self, username)

    def get_user_cart(self, customer):
        return customer.cart

    def get_user_balance(self, customer):
        return customer.balance
