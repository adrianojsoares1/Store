from Web_Store.Store import Store


def login_menu():
    while True:
        print("Welcome to <store_name>.")
        user = input("Please log in.\nEnter username:")
        pss = input("Enter password:")
        s.user_login(user, pss)


if __name__ == "__main__":
    s = Store()
    login_menu()



