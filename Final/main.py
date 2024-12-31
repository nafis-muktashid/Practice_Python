from customer import Customer
from admin import Admin
from restaurant import Resturant

Garrison = Resturant("Hotel Garrison")

def customer_menu():
    name = input("Enter Your Name: ")

    customer = Garrison.find_customer(name)

    if customer != None:
        while True:
            print("1. View Menu")
            print("2. Place Order")
            print("3. View Past Orders")
            print("4. Check Balance")
            print("5. Add Funds")
            print("6. Exit")

            choice = int(input("Enter Your Choice: "))
            if choice == 1:
                customer.view_menu(Garrison)
            elif choice == 2:
                item_name = input("Enter Item Name: ")
                item_quantity = int(input("Enter item quantity: "))
                customer.place_order(Garrison, item_name, item_quantity)
            elif choice == 3:
                customer.view_past_orders()
            elif choice == 4:
                customer.check_balance()
            elif choice == 5:
                amount = int(input("Enter the amount: "))
                customer.add_funds(amount)
            elif choice == 6:
                break
            else:
                print("Invalid Option")
    else:
        print("Please Register First")



def admin_menu():
    name = input("Enter Your Name: ")
    email = input("Enter Your Email: ")
    admnID = input("Enter Your Admin ID: ")

    admin = Admin(name=name, email=email, adminId=admnID)

    print(f"Welcome {admin.name}")
    while True:
        print("1. Add New Item")
        print("2. Add New Customer")
        print("3. View Customer")
        print("4. View Menu Item")
        print("5. Delete Item")
        print("6. Modify Item")
        print("7. Exit")

        choice = int(input("Enter Your Choice: "))
        if choice == 1:
            admin.add_item(Garrison)
        elif choice == 2:
            admin.add_customer(Garrison)
        elif choice == 3:
            admin.view_customer(Garrison)
        elif choice == 4:
            admin.show_items(Garrison)
        elif choice == 5:
            item_name = input("Enter Item Name: ")
            admin.delete_item(Garrison, item_name)
        elif choice == 6:
            admin.modify_item(Garrison)
        elif choice == 7:
            break
        else:
            print("Invalid Option")
            

while True:
    print("Welcome!!")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")

    choice = int(input("Enter Your Choice: "))
    if choice == 1:
        customer_menu()
    elif choice == 2:
        admin_menu()
    elif choice == 3:
        break
    else:
        print("Invalid Input!!!")