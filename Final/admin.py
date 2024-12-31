from customer import Customer
from restaurant import Item


class  Admin:
    def __init__(self, name, email, adminId):
        self.name = name
        self.email = email
        self.adminId = adminId

    def add_item(self, resturant):
        name = input("Enter Item Name: ")
        price = float(input("Set Item Price: "))
        quantity = int(input("Enter Item quantity"))

        item = Item(name, price, quantity)
        resturant.menu.add_item(item)

    def delete_item(self, resturant, item_name):
        resturant.menu.remove_item(item_name)

    def add_customer(self, resturant):
        name = input("Enter Name: ")
        email = input("Enter Customer Email: ")
        address = input("Enter Customer Address: ")
        balance = int(input("Enter Initial balance: "))
        cus = Customer(name, email, address, balance)
        resturant.add_customer(cus)

    def remove_customer(self,  resturant, customer):
        resturant.remove_customer(customer)
        
    def view_customer(self, resturant):
        print("Registered Customer's List!")
        resturant.view_customer()

    def modify_item(self, resturant):
        print("What do you want to modify:")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Update Item Price")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            self.add_item(resturant)
        elif choice == 2:
            item_name = input("Enter Item Name: ")
            resturant.menu.remove_item(item_name)
        elif choice == 3:
            resturant.menu.show_menu()
            item_name = input("Enter Item Name: ")
            new_price = int(input(f"Enter new price of {item_name}: "))
            resturant.menu.update_price(item_name, new_price)
        else:
            print("Invalid choice")

    def show_items(self, resturant):
        resturant.menu.show_menu()