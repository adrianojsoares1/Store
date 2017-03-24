from Web_Store.Store import Store
from Web_Store.Administrator import Administrator
from Web_Store.Customer import Customer
from Web_Store.Physical_Product import Physical_Product
from Web_Store.Digital_Product import Digital_Product
from Web_Store.Subscription_Product import Subscription_Product
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
    print("Main Menu.")
    while True:
        choice = int(input("\nEnter 1 to shop\nEnter 2 to add money\nEnter 3 to change password\nEnter 4 to view cart\n"
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
    print("\nShop Menu.")
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
    print("\nMain Menu.\n")
    while True:
        choice = int(input("1.Add category\n2.Delete category\n3.Set a price\n4.Add a product\n5.Delete a product\n"
                           "6.View Logs\n7.Set Product Category\n8.Quit\n\nEnter:"))
        if choice == 1:
            add_category_menu()
        elif choice == 2:
            delete_category_menu()
        elif choice == 3:
            set_price_menu()
        elif choice == 4:
            add_item_menu()
        elif choice == 5:
            delete_item_menu()
        elif choice == 6:
            pass
        elif choice == 7:
            set_category_menu()
        elif choice == 8:
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
    new_cat = input("\nEnter category to delete:")
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
    name = input("\nEnter product name:")
    new_price = int(input("Enter new price:"))
    for i in s.categories:
        for j in s.categories[i]:
            for k in s.categories[i][j]:
                if k.get_name() == name:
                    k.set_price(new_price)
                    return True
    print("Not found.")
    return False


def set_category_menu():
    name = input("\nEnter product name:")
    new_cat = input("Enter new category:")
    for i in s.categories:
        for j in s.categories[i]:
            for k in s.categories[i][j]:
                if k.get_name() == name:
                    k.set_category(new_cat)
                    return True
    print("Not found.")
    return False


def delete_item_menu():
    name = input("\nEnter product name:")
    for i in s.categories:
        for j in s.categories[i]:
            for k in s.categories[i][j]:
                if k.get_name() == name:
                    s.categories[i][j].remove(k)
                    return True
    print("Not found.")
    return False


def add_item_menu():
    name = input("\nEnter product name:")
    desc = input("Enter product description:")
    price = int(input("Enter item price:"))

    kind = int(input("Is new product...\n1.Physical\n2.Subscription\n3.Digital\nEnter:"))
    if kind == 1:
        quant = int(input("Enter quantity:"))
        while True:
            cat = input("Enter category:")
            if s.categories["Physical"].get(cat) is not None:
                s.categories["Physical"][cat].append(Physical_Product(quant, name, desc, price, cat))
                break
            else:
                print("Invalid Category.")
    elif kind == 2:
        while True:
            lng = int(input("Enter subscription length:"))
            key = input("Enter product download key:")
            cat = input("Enter category:")
            if s.categories["Subscription"].get(cat) is not None:
                s.categories["Subscription"][cat].append(Subscription_Product(name, desc, price, cat, lng, key))
                break
            else:
                print("Invalid Category.")
    elif kind == 3:
        quant = int(input("Enter product code:"))
        while True:
            cat = input("Enter category:")
            if s.categories["Digital"].get(cat) is not None:
                s.categories["Digital"][cat].append(Physical_Product(name, desc, price, cat, None, quant))
                break
            else:
                print("Invalid Category.")


if __name__ == "__main__":
    s.add_administrator("me", "pass")
    if login_menu():
        if type(s.current_user) is Administrator:
            admin_menu()
        elif type(s.current_user) is Customer:
            customer_main_menu()

