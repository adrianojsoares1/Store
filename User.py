from .Product import Product
from .Digital_Product import Digital_Product
from .Physical_Product import Physical_Product
from .Subscription_Product import Subscription_Product

class User:

    def __init__(self):
        self.balance = 0
        self.purchase_history = ["None"]

    def add_money(self, amount):
        self.balance += amount

    def add_review(self, product, review):
        product.add_review(review)


