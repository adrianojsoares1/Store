class Product(object):
    def __init__(self, name="null", description="none", price=-999, category="none", delivery="none",
                 image=None):
        self.name = name
        self.description = description
        self.price = price
        self.reviews = ["None"]
        self.category = category
        self.delivery = delivery
        self.image = image

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_price(self):
        return self.price

    def get_review(self):
        return self.reviews

    def get_category(self):
        return self.category

    def get_delivery(self):
        return self.delivery

    def get_image(self):
        return self.image

    def set_name(self, stri):
        self.name = stri

    def set_description(self, stri):
        self.description = stri

    def set_price(self, integer):
        self.price = integer

    def add_review(self, rev):
        if self.reviews[0] == "None":
            self.reviews[0] = rev
        else:
            self.reviews.append(rev)

    def set_category(self, str):
        self.category = str

    def set_delivery(self, str):
        self.delivery = str

    def set_image(self, img):
        self.image = img

    def to_string(self):
        return "Name", self.name, "\nPrice", self.price, "\nDepartment", self.category

    def valid_class(self):
        return True
