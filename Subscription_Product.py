from Web_Store.Product import Product
import datetime
from datetime import date


class Subscription_Product(Product):

    def __init__(self, name="null", description="none", price=-999, category="none", delivery="none",
                 image=None, subscription_length = -1, download_link = "null", Product_Key = "null"):

        Product.__init__(self,name,description,price,category,"instant",image)

        self.sub_length = subscription_length
        self.download_link = download_link
        self.product_key = Product_Key
        now = datetime.datetime.utcnow()
        self.start_date = date(now.year, now.month, now.day)

    def get_length(self):
        return self.sub_length

    def set_length(self, new_length):
        self.sub_length = new_length

    def get_link(self):
        return self.download_link

    def set_link(self, new_link):
        self.download_link = new_link

    def calc_remaining_time(self):
        temp = datetime.datetime.utcnow()
        return (date(temp.year, temp.month, temp.day) - self.start_date).days

    def is_expired(self):
        return self.calc_remaining_time() > 0

    def renew(self, days):
        temp = datetime.datetime.utcnow()
        self.sub_length = self.calc_remaining_time() + days
        self.start_date = date(temp.year, temp.month, temp.day)
