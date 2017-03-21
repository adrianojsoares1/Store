from .Product import Product


class Physical_Product(Product):

    def __init__(self, quantity=0, name="null", description="none", price=-999, category="none",
                 image=None, ship_time=-1, weight=0):
        Product.__init__(self, name, description, price, category, "shipping", image)
        self.ship_time = ship_time
        self.weight = weight
        self.quantity = quantity

    def get_ship_time(self):
        return self.ship_time

    def set_ship_time(self, new_time):
        self.ship_time = new_time
