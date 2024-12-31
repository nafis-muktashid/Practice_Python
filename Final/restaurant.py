class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Menu:
    def  __init__(self):
        self.items = []

    def show_menu(self):
        print("----------MENU----------")
        print("Name\tPrice\tQuantity")
        for item in self.items:
            print(f"{item.name}\t{item.price}\t{item.quantity}")

    def find_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None
    
    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            print("Item Removed!")
        else:
            print("Item Not Found!")

    def update_price(self, item_name, new_price):
        item = self.find_item(item_name)
        item.price = new_price

class Resturant:
    def __init__(self, name):
        self.name = name
        self.customers = []
        self.menu = Menu()

    def add_customer(self, customer):
        self.customers.append(customer)

    def remove_customer(self, customer):
        self.menu.items.remove(customer)
        
    def view_customer(self):
        print("All the Registered Customers----")
        print(f"Name\tEmail\tAddress\tBalance")
        for e in self.customers:
            print(f"{e.name}\t{e.email}\t{e.address}\t{e.balance}")

    def find_customer(self, name):
        for c in self.customers:
            if c.name.lower() == name.lower():
                return c
        return None

    

