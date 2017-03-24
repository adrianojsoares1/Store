from .Product import Product


class Physical_Product(Product):

    def __init__(self, quantity=0, name="null", description="none", price=-999, category="none",
                 image=None):
        Product.__init__(self, name, description, price, category, "shipping", image)
        self.quantity = quantity

    def set_quantity(self, new):
        self.quantity = new

    def get_quantity(self):
        return self.quantity

    def buy_1(self):
        self.quantity -= 1
