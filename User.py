class User(object):

    def __init__(self, username):
        self._username = username
        self._last_login_time = ""
        self._last_logout_time = ""

    def set_user(self, new_name):
        self._username = new_name

    def get_username(self):
        return self._username

    def add_product_review(self, product, string):
        product.add_review(self._username, "says:", string)
