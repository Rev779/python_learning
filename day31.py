"""Restaurant Management System - OOP project with interactive menu."""
from abc import ABC, abstractmethod
from datetime import datetime


# ---------- Menu (Abstraction + Inheritance) ----------
class MenuItem(ABC):
    def __init__(self, item_id, name, price):
        self.item_id = item_id
        self.name = name
        self.__price = price  # encapsulated

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Price must be positive")
        self.__price = value

    @abstractmethod
    def category(self):
        pass

    def __str__(self):
        return f"{self.item_id:>3}. {self.name:<20} {self.category():<10} Rs.{self.price:.2f}"


class Food(MenuItem):
    def __init__(self, item_id, name, price, veg=True):
        super().__init__(item_id, name, price)
        self.veg = veg

    def category(self):
        return "Veg" if self.veg else "Non-Veg"


class Beverage(MenuItem):
    def category(self):
        return "Beverage"

class Menu:
    def __init__(self):
        self._items = {}
        self._next_id = 1

    def add_item(self, name, price, kind, veg=True):
        item_id = self._next_id
        if kind == "1":
            item = Food(item_id, name, price, veg)
        else:
            item = Beverage(item_id, name, price)
        self._items[item_id] = item
        self._next_id += 1
        return item

    def remove_item(self, item_id):
        return self._items.pop(item_id, None)

    def get(self, item_id):
        if item_id not in self._items:
            raise KeyError(f"Item {item_id} not on menu")
        return self._items[item_id]

    def show(self):
        if not self._items:
            print("Menu is empty.")
            return
        print("\n--- MENU ---")
        for item in self._items.values():
            print(item)


# ---------- Staff (Polymorphism) ----------
class Staff(ABC):
    def __init__(self, staff_id, name):
        self.staff_id = staff_id
        self.name = name

    @abstractmethod
    def role(self):
        pass

    def __str__(self):
        return f"{self.staff_id:>3}. {self.name} ({self.role()})"


class Waiter(Staff):
    def role(self):
        return "Waiter"


class Chef(Staff):
    def role(self):
        return "Chef"


class Manager(Staff):
    def role(self):
        return "Manager"


# ---------- Table ----------
class Table:
    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity
        self.is_free = True

    def __str__(self):
        status = "Free" if self.is_free else "Occupied"
        return f"Table {self.number:>2} | Capacity {self.capacity} | {status}"


# ---------- Order & Bill (Composition) ----------
class Order:
    _next_id = 1

    def __init__(self, table, waiter):
        self.order_id = Order._next_id
        Order._next_id += 1
        self.table = table
        self.waiter = waiter
        self.lines = []  # list of (MenuItem, quantity)
        self.status = "PLACED"
        self.time = datetime.now()

    def add_item(self, item, qty=1):
        self.lines.append((item, qty))

    def subtotal(self):
        return sum(item.price * qty for item, qty in self.lines)

    def update_status(self, status):
        self.status = status

    def __str__(self):
        lines_str = ", ".join(f"{item.name} x{qty}" for item, qty in self.lines)
        return (f"Order #{self.order_id} | Table {self.table.number} | "
                f"Waiter: {self.waiter.name} | Status: {self.status} | Items: {lines_str}")


class Bill:
    GST_RATE = 0.05

    def __init__(self, order, discount_percent=0):
        self.order = order
        self.discount_percent = discount_percent

    def total(self):
        sub = self.order.subtotal()
        discount = sub * self.discount_percent / 100
        tax = (sub - discount) * self.GST_RATE
        return sub, discount, tax, sub - discount + tax

    def print_bill(self):
        sub, discount, tax, total = self.total()
        print(f"\n===== BILL (Order #{self.order.order_id}, Table {self.order.table.number}) =====")
        for item, qty in self.order.lines:
            print(f"{item.name:<20} x{qty}  Rs.{item.price * qty:.2f}")
        print(f"Subtotal : Rs.{sub:.2f}")
        print(f"Discount : Rs.{discount:.2f}")
        print(f"GST (5%) : Rs.{tax:.2f}")
        print(f"TOTAL    : Rs.{total:.2f}")


# ---------- Restaurant (ties everything together) ----------
class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = Menu()
        self.tables = {}
        self.staff = []
        self.orders = []
        self.sales = 0.0

    def add_table(self, number, capacity):
        self.tables[number] = Table(number, capacity)

    def show_tables(self):
        if not self.tables:
            print("No tables added yet.")
            return
        print("\n--- TABLES ---")
        for table in self.tables.values():
            print(table)

    def hire(self, staff_id, name, role):
        if role == "1":
            staff = Waiter(staff_id, name)
        elif role == "2":
            staff = Chef(staff_id, name)
        else:
            staff = Manager(staff_id, name)
        self.staff.append(staff)
        return staff

    def show_staff(self):
        if not self.staff:
            print("No staff hired yet.")
            return
        print("\n--- STAFF ---")
        for s in self.staff:
            print(s)  # polymorphism: each prints its own role

    def find_waiter(self, staff_id):
        for s in self.staff:
            if isinstance(s, Waiter) and s.staff_id == staff_id:
                return s
        return None

    def place_order(self, table_no, waiter):
        table = self.tables.get(table_no)
        if table is None:
            print("Table not found.")
            return None
        if not table.is_free:
            print(f"Table {table_no} is occupied.")
            return None
        table.is_free = False
        order = Order(table, waiter)
        self.orders.append(order)
        return order

    def show_orders(self):
        if not self.orders:
            print("No orders yet.")
            return
        print("\n--- ORDERS ---")
        for order in self.orders:
            print(order)

    def find_order(self, order_id):
        for order in self.orders:
            if order.order_id == order_id:
                return order
        return None

    def checkout(self, order, discount_percent=0):
        order.update_status("PAID")
        bill = Bill(order, discount_percent)
        bill.print_bill()
        self.sales += bill.total()[3]
        order.table.is_free = True

    def daily_report(self):
        print(f"\n{self.name} - Orders: {len(self.orders)}, Sales: Rs.{self.sales:.2f}")


# ---------- Interactive Menu ----------
def add_menu_item(restaurant):
    name = input("Enter Item Name: ")
    try:
        price = float(input("Enter Price: "))
    except ValueError:
        print("Invalid price. Item not added.")
        return
    kind = input("Is it Food or Beverage? (1-Food / 2-Beverage): ")
    veg = True
    if kind == "1":
        veg_input = input("Veg or Non-Veg? (v/n): ").strip().lower()
        veg = veg_input != "n"
    restaurant.menu.add_item()
    print("Menu item added successfully!")


def add_table(restaurant):
    try:
        number = int(input("Enter Table Number: "))
        capacity = int(input("Enter Table Capacity: "))
    except ValueError:
        print("Invalid input. Table not added.")
        return
    restaurant.add_table(number, capacity)
    print("Table added successfully!")


def hire_staff(restaurant):
    try:
        staff_id = int(input("Enter Staff ID: "))
    except ValueError:
        print("Invalid ID.")
        return
    name = input("Enter Staff Name: ")
    role = input("Select Role (1-Waiter / 2-Chef / 3-Manager): ")
    restaurant.hire(staff_id, name, role)
    print("Staff hired successfully!")


def place_order(restaurant):
    try:
        table_no = int(input("Enter Table Number: "))
        waiter_id = int(input("Enter Waiter ID: "))
    except ValueError:
        print("Invalid input.")
        return
    waiter = restaurant.find_waiter(waiter_id)
    if waiter is None:
        print("Waiter not found.")
        return
    order = restaurant.place_order(table_no, waiter)
    if order is None:
        return
    while True:
        restaurant.menu.show()
        item_choice = input("Enter Item ID to add (or 'done' to finish): ")
        if item_choice.lower() == "done":
            break
        try:
            item = restaurant.menu.get(int(item_choice))
        except (ValueError, KeyError):
            print("Item not found.")
            continue
        try:
            qty = int(input("Enter Quantity: "))
        except ValueError:
            qty = 1
        order.add_item(item, qty)
        print(f"Added {item.name} x{qty} to order.")
    if not order.lines:
        print("No items added. Order cancelled.")
        restaurant.orders.remove(order)
        order.table.is_free = True
        return
    print(f"Order placed successfully! Order ID: {order.order_id}")


def checkout_order(restaurant):
    try:
        order_id = int(input("Enter Order ID to checkout: "))
    except ValueError:
        print("Invalid Order ID.")
        return
    order = restaurant.find_order(order_id)
    if order is None:
        print("Order not found.")
        return
    if order.status == "PAID":
        print("Order already paid.")
        return
    try:
        discount = float(input("Enter Discount % (0 if none): "))
    except ValueError:
        discount = 0
    restaurant.checkout(order, discount)


def main():
    restaurant = Restaurant("Spice Garden")
    while True:
        print("\n===== RESTAURANT MANAGEMENT SYSTEM =====")
        print("1. Add Menu Item")
        print("2. Display Menu")
        print("3. Add Table")
        print("4. Display Tables")
        print("5. Hire Staff")
        print("6. Display Staff")
        print("7. Place Order")
        print("8. Display Orders")
        print("9. Checkout / Generate Bill")
        print("10. Daily Report")
        print("11. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_menu_item(restaurant)
        elif choice == "2":
            restaurant.menu.show()
        elif choice == "3":
            add_table(restaurant)
        elif choice == "4":
            restaurant.show_tables()
        elif choice == "5":
            hire_staff(restaurant)
        elif choice == "6":
            restaurant.show_staff()
        elif choice == "7":
            place_order(restaurant)
        elif choice == "8":
            restaurant.show_orders()
        elif choice == "9":
            checkout_order(restaurant)
        elif choice == "10":
            restaurant.daily_report()
        elif choice == "11":
            print("Thank you!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()