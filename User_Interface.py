from Web_Store.Store import Store

s = Store()


def login_menu():
    while True:
        print("Welcome to <store_name>.")
        choice = int(input("Enter 1 to login.\nEnter 2 to create new account.\nEnter 3 to quit.\nEnter:"))
        if choice == 1:
            user = input("Please log in.\nEnter username:")
            pss = input("Enter password:")
            a_str = s.user_login(user, pss)
            if a_str == "Login Successful":
                return True
            print(a_str)
        elif choice == 2:
            while True:
                user = input("Welcome.\nChoose a username:")
                pass1 = input("Enter a password:")
                pass2 = input("Confirm password:")
                if pass1 == pass2:
                    print("Welcome to <store_name>,", user, '!')
                    s.add_customer(user, pass1)
                    break
                else:
                    print("Passwords did not match!")
        elif choice == 3:
            return False


def customer_main_menu():
    choice = int(input("Enter 1 to shop\nEnter 2 to add money\nEnter 3 to change password\nEnter 4 to view cart\n"
                       "\nEnter 6 to logout."))
    while True:
        if choice == 1:
            shop_menu()
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        elif choice == 5:
            pass

def admin_main_menu():


def shop_menu():
    dictry = s.get_categories()
    count = 1
    for i in dictry:
        for j in dictry[i]:
            print("Enter", count, "for", j)
            count += 1
    choice = input("Enter:")

def add_money_menu():
    print("Your current account balance is:", s.current_user.get_balance())
    ad = int(input())


if __name__ == "__main__":
    if login_menu():
        if type(s.current_user) == "Administrator":
            admin_main_menu()
        elif type(s.current_user) == "Customer":
            customer_main_menu()
