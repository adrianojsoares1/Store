from .Product import Product


class Digital_Product(Product):

    def __init__(self, quantity=0, name="null", description="none", price=-999, category="none",
                 image=None, code="invalid_code"):
        Product.__init__(self, name, description, price, category, "instant", image)
        self.code = code

    def get_code(self):
        return self.code

    def set_code(self, new_code):
        self.code = new_code
