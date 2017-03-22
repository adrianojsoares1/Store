from .User import User


class Administrator(User):

    def __init__(self, username):
        User.__init__(self, username)


