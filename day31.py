"""Restaurant Management System - OOP starter project."""
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

    def add_item(self, item):
        self._items[item.item_id] = item

    def remove_item(self, item_id):
        self._items.pop(item_id, None)

    def get(self, item_id):
        if item_id not in self._items:
            raise KeyError(f"Item {item_id} not on menu")
        return self._items[item_id]

    def show(self):
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
        return f"{self.name} ({self.role()})"


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

    def add_table(self, table):
        self.tables[table.number] = table

    def hire(self, staff):
        self.staff.append(staff)

    def place_order(self, table_no, waiter):
        table = self.tables[table_no]
        if not table.is_free:
            raise RuntimeError(f"Table {table_no} is occupied")
        table.is_free = False
        order = Order(table, waiter)
        self.orders.append(order)
        return order

    def checkout(self, order, discount_percent=0):
        order.update_status("PAID")
        bill = Bill(order, discount_percent)
        bill.print_bill()
        self.sales += bill.total()[3]
        order.table.is_free = True

    def daily_report(self):
        print(f"\n{self.name} - Orders: {len(self.orders)}, Sales: Rs.{self.sales:.2f}")


# ---------- Demo ----------
if __name__ == "__main__":
    r = Restaurant("Spice Garden")
    r.menu.add_item(Food(1, "Paneer Butter Masala", 220, veg=True))
    r.menu.add_item(Food(2, "Chicken Biryani", 280, veg=False))
    r.menu.add_item(Beverage(3, "Masala Chai", 30))
    r.add_table(Table(1, 4))
    r.add_table(Table(2, 2))

    waiter = Waiter(101, "RAMESH")
    r.hire(waiter)
    r.hire(Chef(102, "AJITH"))
    r.hire(Manager(103, "REVANTH"))
    for s in r.staff:
        print(s)  # polymorphism: each prints its own role

    r.menu.show()

    order = r.place_order(1, waiter)
    order.add_item(r.menu.get(2), 2)
    order.add_item(r.menu.get(3), 2)
    order.update_status("SERVED")

    r.checkout(order, discount_percent=10)
    r.daily_report()