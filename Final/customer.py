class Order:
    def __init__(self):
        self.items = {}

    def add_item(self, item):
        if item.name in self.items:
            self.items[item.name] += item.quantity
        else:
            self.items[item.name] = item.quantity

    def remove(self, item):
        if item in self.items:
            del self.items[item]
    @property
    def total_price(self):
        return sum(item.price * quantity for item,quantity in self.items.items())

    def clear(self):
        self.items = {}


class Customer:
    def __init__(self, name, email, address, balance):
        self.name = name
        self.email = email
        self.address = address
        self.balance = balance
        self.cart = Order()
        self.past_orders = []

    def view_menu(self, resturant):
            resturant.menu.show_menu()
    def place_order(self, restaurant, item_name, quantity):

        item = restaurant.menu.find_item(item_name)
        if not item:
            print("No Item Found")
            return

        if quantity <= item.quantity and item.price * quantity <= self.balance:
            self.balance -= item.price * quantity
            item.quantity -= quantity
            self.cart.add_item(item)
            self.past_orders.append({item.name, quantity})
            print("Order Placed Successfully!")
        else:
            if quantity > item.quantity:
                print("Item quantity exceeded")
            if item.price * quantity > self.balance:
                print("Not Enough Balance")

    
    def view_past_orders(self):
        print("Past Orders:------------")
        print("Item Name\tQuantity")
        for name, quantity in self.past_orders:
            print(f"{name}\t{quantity}")

    def check_balance(self):
        print(f"Customer Name: {self.name} , Balance: {self.balance}")

    def add_funds(self, amount):
        self.balance += amount
        print(f"{amount} added to balance. New balance: {self.balance}")