from .Product import Product
from .Digital_Product import Digital_Product
from .Physical_Product import Physical_Product
from .Subscription_Product import Subscription_Product


class User:

    def __init__(self):
        self.cart = []

    def add_to_cart(self, item):
        self.cart.append(item)

    def delete_from_cart(self, item):
        self.cart.remove(item)
