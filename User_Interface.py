from Web_Store.Store import Store
from Web_Store.Administrator import Administrator
from Web_Store.Customer import Customer

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
    while True:
        choice = int(input("Enter 1 to shop\nEnter 2 to add money\nEnter 3 to change password\nEnter 4 to view cart\n"
                           "Enter 5 to logout."))
        if choice == 1:
            shop_menu()
        elif choice == 2:
            add_money_menu()
        elif choice == 3:
            change_pass_menu()
        elif choice == 4:
            view_cart_menu()
        elif choice == 5:
            break


def shop_menu():
    dictry = s.get_categories()
    count = 1
    keys = []
    for i in dictry:
        for j in dictry[i]:
            print(count, ".", j)
            keys.append(j)
            count += 1
    choice = int(input("Enter:"))

    chosen_item_str = keys[choice - 1]

    sub_cat = []
    for i in dictry:
        if dictry[i].get(chosen_item_str) is not None:
            sub_cat = dictry[i][chosen_item_str]

    for i in range(0, len(sub_cat)):
        print((i + 1), ".", sub_cat[i].to_string())

    choice = int(input("Enter:"))

    if choice in range(1, len(sub_cat)):
        print(sub_cat[choice - 1].toString())

    add2cart = int(input("1. to add to cart\n2. Go back.\nEnter:"))
    if add2cart == 1:
        s.current_user.add_to_cart(sub_cat[choice - 1])


def add_money_menu():
    print("Your current account balance is:", s.current_user.get_balance())
    ad = int(input("Enter money to add:"))
    s.current_user.add_to_balance(ad)


def change_pass_menu():
    while True:
        pw = input("Enter your current password:")
        if s.login(s.current_user.get_username(), pw):
            nw_pw = input("Enter new password:")
            s.change_user_password(nw_pw)
            break
        else:
            print("Current password is incorrect.")


def view_cart_menu():
    tmp = s.current_user.get_cart()
    print("Cart for user", s.current_user.get_username(), ":")
    for i in range(1, len(tmp)):
        print(i, ".", tmp[i])

    print("1. Checkout (Your total comes to: $", s.current_user.get_cart_total(), ")\n2. Quit")
    imp = int(input("Enter: "))
    if imp == 1:
        s.current_user.purchase()


def admin_menu():
    while True:
        choice = int(input("1.Add category\n2.Delete category\n3.Set a price\n4.View Logs\n5.Set Product Category"))
        if choice == 1:
            add_category_menu()
        elif choice == 2:
            delete_category_menu()
        elif choice == 3:
            set_price_menu()
        elif choice == 4:
            pass
        elif choice == 5:
            set_category_menu()
        elif choice == 6:
            break


def add_category_menu():
    while True:
        master_cat = int(input("Is new category...\n1.Physical\n2.Subscription\n3.Digital\n4.Go back\nEnter:"))
        new_cat = input("Enter new category:")
        if master_cat == 1:
            s.add_category("Physical", new_cat)
            break
        elif master_cat == 2:
            s.add_category("Subscription", new_cat)
            break
        elif master_cat == 3:
            s.add_category("Digital", new_cat)
            break
        elif master_cat == 4:
            break
        print(new_cat, "was added as a category.")


def delete_category_menu():
    new_cat = input("Enter category to delete:")
    tmpi = ""
    tmpj = ""
    for i in s.categories:
        for j in s.categories[i]:
            if j == new_cat:
                tmpj = j
                tmpi = i
    if tmpi != "" and tmpj != "":
        del s.categories[tmpi][tmpj]
    else:
        print("Did not find category.")


def set_price_menu():
    name = input("Enter product name:")
    new_price = int(input("Enter new price:"))
    for i in s.categories:
        for j in s.categories[i]:
            for k in s.categories[i][j]:
                if k.get_name() == name:
                    k.set_price(new_price)
    print("Not found.")


def set_category_menu():
    name = input("Enter product name:")
    new_cat = input("Enter new category:")
    for i in s.categories:
        for j in s.categories[i]:
            for k in s.categories[i][j]:
                if k.get_name() == name:
                    k.set_category(new_cat)
    print("Not found.")


def delete_item_menu():
    name = input("Enter product name:")
    for i in s.categories:
        for j in s.categories[i]:
            for k in s.categories[i][j]:
                if k.get_name() == name:
                    s.categories[i][j].remove(k)
    print("Not found.")


def add_item_menu():
    name = input("Enter product name:")


if __name__ == "__main__":
    s.add_administrator("me", "pass")
    if login_menu():
        if type(s.current_user) is Administrator:
            admin_menu()
        elif type(s.current_user) is Customer:
            customer_main_menu()

