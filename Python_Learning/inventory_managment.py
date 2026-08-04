class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.__price = price          # Encapsulation
        self.quantity = quantity

    def get_price(self):
        return self.__price

    def update_price(self, new_price):
        self.__price = new_price

    def display(self):
        print(f"{self.product_id} | {self.name} | Price: {self.__price} | Qty: {self.quantity}")


class Electronics(Product):           # Inheritance
    def __init__(self, product_id, name, price, quantity, warranty):
        super().__init__(product_id, name, price, quantity)
        self.warranty = warranty

    def display(self):                # Polymorphism
        print(f"Electronics -> {self.name}, Price: {self.get_price()}, Warranty: {self.warranty} Years")


class Grocery(Product):
    def __init__(self, product_id, name, price, quantity, expiry):
        super().__init__(product_id, name, price, quantity)
        self.expiry = expiry

    def display(self):
        print(f"Grocery -> {self.name}, Price: {self.get_price()}, Expiry: {self.expiry}")


class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name

    def display(self):
        print(f"Customer ID: {self.customer_id}")
        print(f"Customer Name: {self.name}")


class Order:
    def __init__(self, order_id, customer):
        self.order_id = order_id
        self.customer = customer
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def total_bill(self):
        total = 0
        for product in self.products:
            total += product.get_price()
        return total

    def display_order(self):
        print("\n------ Order Details ------")
        self.customer.display()

        print("\nProducts:")
        for product in self.products:
            product.display()

        print(f"\nTotal Bill = {self.total_bill()}")


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def show_inventory(self):
        print("\n------ Inventory ------")
        for product in self.products:
            product.display()


# ---------------- Main Program ----------------

inventory = Inventory()

laptop = Electronics(101, "Dell Laptop", 85000, 5, 2)
mobile = Electronics(102, "iPhone", 180000, 3, 1)
rice = Grocery(201, "Rice Bag", 3500, 20, "12-2026")

inventory.add_product(laptop)
inventory.add_product(mobile)
inventory.add_product(rice)

inventory.show_inventory()

customer = Customer(1, "Ali")

order = Order(1001, customer)

order.add_product(laptop)
order.add_product(rice)

order.display_order()