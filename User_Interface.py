from Web_Store.Store import Store
from Web_Store.Administrator import Administrator
from Web_Store.Customer import Customer
from Web_Store.Physical_Product import Physical_Product
from Web_Store.Digital_Product import Digital_Product
from Web_Store.Subscription_Product import Subscription_Product
s = Store()


def login_menu():
    while True:
        print("Welcome to the Store.")
        choice = int(input("Enter 1 to login.\nEnter 2 to create new account.\nEnter 3 to quit.\nEnter:"))
        if choice == 1:
            user = input("Please log in.\nEnter username:")
            pss = input("Enter password:")
            a_str = s.user_login(user, pss)
            if a_str == "Login Successful":
                print(a_str, '.')
                return True
            print(a_str)
        elif choice == 2:
            while True:
                user = input("Welcome.\nChoose a username:")
                pass1 = input("Enter a password:")
                pass2 = input("Confirm password:")
                if pass1 == pass2:
                    print("Welcome to the store" + str(user) + '!')
                    s.add_customer(user, pass1)
                    break
                else:
                    print("Passwords did not match!")
        elif choice == 3:
            return False


def customer_main_menu():
    while True:
        print("\nMain Menu.\n")
        choice = int(input("Enter 1 to shop\nEnter 2 to add money\nEnter 3 to change password\nEnter 4 to view cart\n"
                           "Enter 5 to logout.\n\nEnter:"))
        if choice == 1:
            shop_menu()
        elif choice == 2:
            add_money_menu()
        elif choice == 3:
            change_pass_menu()
        elif choice == 4:
            view_cart_menu()
        elif choice == 5:
            s.user_logout()
            break


def shop_menu():
    while True:
        print("Shop Menu.")
        dictry = s.get_categories()
        count = 1
        keys = []
        print("0 . Go Back")
        for i in dictry:
            for j in dictry[i]:
                print(count, ".", j)
                keys.append(j)
                count += 1

        choice = int(input("Enter:"))

        if choice == 0:
            break

        chosen_item_str = keys[choice - 1]

        sub_cat = []
        for i in dictry:
            if dictry[i].get(chosen_item_str) is not None:
                sub_cat = dictry[i][chosen_item_str]

        for i in range(0, len(sub_cat)):
            print((i + 1), ".", sub_cat[i].to_string())
        while True:
            choice = int(input("0 . Go Back\nEnter:"))
            if choice == 0:
                break

            if choice in range(0, (1 + len(sub_cat))):
                print(sub_cat[choice - 1].to_string())

            add2cart = int(input("1. to add to cart\n2. Go back.\nEnter:"))
            if add2cart == 1:
                if type(sub_cat[choice - 1]) is Physical_Product and sub_cat[choice - 1].get_quantity() == 0:
                    print("Out of Stock!")
                    break
                else:
                    s.current_user.add_to_cart(sub_cat[choice - 1])
                    print("Item added to cart!")
                    break
            elif add2cart == 2:
                break


def add_money_menu():
    print("Your current account balance is:", s.current_user.get_balance())
    ad = int(input("Enter money to add:"))
    s.current_user.add_to_balance(ad)
    print(ad, "dollars have been deducted from bank account. New balance:", s.current_user.get_balance())


def change_pass_menu():
    while True:
        pw = input("Enter your current password:")
        if s.user_login(s.current_user.get_username(), pw) == "Login Successful":
            nw_pw = input("Enter new password:")
            s.change_user_password(nw_pw)
            print("Password has been changed successfully.")
            break
        else:
            print("Current password is incorrect.")


def view_cart_menu():
    tmp = s.current_user.get_cart()
    print("Cart for user", s.current_user.get_username(), ":")
    if len(tmp) < 1:
        print("Cart is empty!")
    else:
        for i in range(0, len(tmp)):
            print(tmp[i].to_string())

        print("1 . Checkout (Your total comes to: $", s.current_user.get_cart_total(), ")\n2 . Quit")
        imp = int(input("Enter: "))
        if imp == 1:
            s.user_purchase()
            print("Items have been purchased and will be shipped / emailed to you shortly!")



def admin_menu():
    while True:
        print("\nMain Menu.\n")
        choice = int(input("1.Add category\n2.Delete category\n3.Set a price\n4.Add a product\n5.Delete a product\n"
                           "6.View Logs\n7.Set Product Category\n8.Restock item\n9.Quit\n\nEnter:"))
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
            view_logs_menu()
        elif choice == 7:
            set_category_menu()
        elif choice == 8:
            restock_item_menu()
        elif choice == 9:
            s.user_logout()
            break


def add_category_menu():
    while True:
        master_cat = int(input("Is new category...\n1.Physical\n2.Subscription\n3.Digital\n4.Go back\nEnter:"))
        new_cat = input("Enter new category:")
        if master_cat == 1:
            s.add_category("Physical", new_cat)
            print(new_cat, "was added as a category.")
            break
        elif master_cat == 2:
            s.add_category("Subscription", new_cat)
            print(new_cat, "was added as a category.")
            break
        elif master_cat == 3:
            s.add_category("Digital", new_cat)
            print(new_cat, "was added as a category.")
            break
        elif master_cat == 4:
            break


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
        print(new_cat, "was deleted as a category.")
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
                    temp = k.get_price()
                    print("New price for", name, ":", temp)
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
                    for f in s.categories[i]:
                        if new_cat == f:
                            k.set_category(new_cat)
                            s.categories[i][j].remove(k)
                            s.categories[i][f].append(k)
                            temp = k.get_category()
                            print("New Category for", name, ":", temp)
                            return True
                    else:
                        print("New category doesn't exist.")
                        return False
    print("Not found.")
    return False


def delete_item_menu():
    name = input("\nEnter product name:")
    for i in s.categories:
        for j in s.categories[i]:
            for k in s.categories[i][j]:
                if k.get_name() == name:
                    s.categories[i][j].remove(k)
                    print(name, "has been deleted from", j)
                    return True
    print("Not found.")
    return False


def restock_item_menu():
    name = input("\nEnter product name:")
    amt = int(input("By how much?:"))
    for i in s.categories:
        for j in s.categories[i]:
            for k in range(0,len(s.categories[i][j])):
                if s.categories[i][j][k].get_name() == name:
                    s.restock(s.categories[i][j][k], amt)
                    temp = s.categories[i][j][k]
                    return True
    print("Not found, or item does not have value \"Stock\".")
    return False

def view_logs_menu():
    print("Item purchase logs: ")
    for i in s.get_purchases():
        print(i)

    print("\nComplete Product Listing: ")
    for i in s.get_products():
        print(i)

    print()
    for i in s.get_activity():
        print(i)

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
                print("Physical_Product object", name, "has been created and added to the category", cat)
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
                print("Subscription_Product object", name, "has been created and added to the category", cat)
                break
            else:
                print("Invalid Category.")
    elif kind == 3:
        quant = int(input("Enter product code:"))
        while True:
            cat = input("Enter category:")
            if s.categories["Digital"].get(cat) is not None:
                s.categories["Digital"][cat].append(Physical_Product(name, desc, price, cat, None, quant))
                print("Digital_Product object", name, "has been created and added to the category", cat)
                break
            else:
                print("Invalid Category.")


if __name__ == "__main__":
    s.add_administrator("me", "pass")
    s.add_customer("adr", "pet")

    products = [
        Physical_Product(100, "Macbook", "2016 Model Macbook Pro.", 2000, "Computers"),
        Physical_Product(100, "Surface Pro", "2016 Model Microsoft Surface Pro.", 1500, "Computers"),

        Physical_Product(100, "ASUS VSQ74", "24 inch 1080p monitor", 100, "Monitors"),
        Physical_Product(100, "BenQ Gaming Monitor", "25 inch 4k monitor", 400, "Monitors"),

        Physical_Product(100, "Python Essentials", "Learn the basics of python with this intuitive guide!", 30,
                         "Textbooks"),
        Physical_Product(100, "Intro to C++", "Learn the basics of C++ and OOP!", 50, "Textbooks"),

        Subscription_Product("Programming Class", "A class to teach programming.", 100, "Classes", None, 90,
                             "a_link.com"),

        Subscription_Product("Malwarebytes", "Defend against malware!", 40, "Anti-virus", None, 90,
                             "malwarebytes.com"),
        Subscription_Product("Norton", "Like malwarebytes, but shittier.", 20, "Anti-virus", None, 90,
                             "symmantec.com"),

        Subscription_Product("Netflix", "Watch cool movies and stuff.", 10, "Video Streaming", None, 30,
                             "netflix.com"),
        Subscription_Product("Prime Video", "Watch lots of movies, discount for prime members!", 10, "Video Streaming",
                             None, 30, "amazon.com"),

        Digital_Product("Amazon Gift Card", "Spend on all your favorite Amazon products.", 30, "Gift Cards", "@c0de"),
        Digital_Product("Outback", "Eat more steak.", 30, "Gift Cards", "steaksrgood"),

        Digital_Product("Skyrim", "Best selling open world RPG of all time.", 20, "Steam Codes", "code"),
        Digital_Product("Dishonored", "Play as an assassin protecting his legacy.", 20, "Steam Codes", "acode"),

        Digital_Product("The Catcher in the Rye", "by JD. Salinger", 20, "E-books", "code"),
        Digital_Product("Hitchhikers Guide to the Galaxy", "by Douglas Adams", 20, "E-books", "code")
    ]
    s.add_administrator("System_Admin", "11000110101010010101110101111")
    s.user_login("System_Admin", "11000110101010010101110101111")
    for i in products:
        s.add_product(i)
    s.user_logout()

    while True:
        if login_menu():
            if type(s.current_user) is Administrator:
                admin_menu()
            elif type(s.current_user) is Customer:
                customer_main_menu()
        else:
            break
