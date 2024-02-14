print("")
print("========CIRCLE==========")
class Circle:

  def __init__(self, radius):
    self.radius = radius

  def find_diameter(self):
    return self.radius * 2


my_circle = Circle(5)

# since it doesn't take arugments on the find_diameter, we don't specify anything below:
diameter = my_circle.find_diameter()
#remember that we have to assign it to a variable!
print(diameter)

print("")
print("========BACKPACK=========")
class Backpack:

  def __init__(self):
    self._items = []

  @property
  def items(self):
    return self._items

# calling a method from another method:
  def add_multiple_items(self, items):
    for item in items:
      self.add_item(item)

  def add_item(self, item):
    if isinstance(item, str):
      self._items.append(item)
    else:
      print("Please provide a valid item.")

  def remove_item(self, item):
    if item in self._items:
      self._items.remove(item)
      return 1
    else:
      print("This item is not in the backpack.")
      return 0

# wil return true or false:
  def has_item(self, item):
    return item in self._items

  def show_items(self, sorted_list=False):
    if sorted_list:
#sorted is python funciton to display things alphabetically:
      print(sorted(self._items))
    else:
      print(self._items)

my_backpack = Backpack()
# my_backpack.add_item("Water Bottle")
# my_backpack.add_item("Sleeping Bag")
# my_backpack.add_item("Candy")

# print("Not Sorted:")
# my_backpack.show_items()

# print("Sorted:")
# my_backpack.show_items(True)

my_backpack.add_multiple_items(["Water Bottle", "Candy", "Sleeping Bag"])
print(my_backpack.items)

# since we've used return, we have to assign the value in to a variable here:
# has_water = my_backpack.has_item("Water Bottle")
# print(has_water)

# my_backpack.remove_item("Water Bottle")
# print(my_backpack.items)
# my_backpack.remove_item("Candy")
# print(my_backpack.items)

print("")
print("========PLAYER==========")
# DEFAULT ARGUMENTS
class Player:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    
  def move_up(self, change=5):
    self.y += change

  def move_down(self, change=5):
    self.y -= change

  def move_right(self, change=2):
    self.x += change

  def move_left(self, change=2):
    self.x -= change

my_player = Player(5, 10)
print(my_player.y)
my_player.move_down()
print(my_player.y)

my_player = Player(5, 10)
print(my_player.x)
my_player.move_left(8)
print(my_player.x)

print("")
print("========CASHREGISTER==========")
class CashRegister:

  TAXES_DECIMAL = 0.05

  def __init__(self, cashier):
    self.cashier = cashier
    self.products = {}

  def add_product(self, new_product, quantity=1):
# new_products is a dictionary.
    self.products[new_product["name"]] = {
      "price": new_product["price"],
      "quantity": quantity
      }

  def show_products(self):
    print(self.products)

  def remove_product(self, product):
  # product is a string with the name of the product.
    del self.products[product]

  def update_price(self, product, new_price):
  # product is a string with the name of the product.
    self.products[product]["price"] = new_price

  def find_subtotal(self):
    subtotal = 0
    for product_info in self.products.values():
        subtotal += product_info["price"] * product_info["quantity"]
    return subtotal

  def print_subtotal(self):
    print(self.find_subtotal())

  def find_taxes(self):
    return round(self.find_subtotal() * CashRegister.TAXES_DECIMAL, 2)

  def print_taxes(self):
    print(f"Taxes: {self.find_taxes()}")

  def find_total(self):
    return round(self.find_subtotal() + self.find_taxes(), 2)

  def print_total(self):
    print(f"Total: {self.find_total()}")

  def clear_purchase(self):
    self.products.clear()


# Create the instance
my_cash_register = CashRegister("Nora")

# Create the products
product_1 = {"name": "Pizza", "price": 3.54}
product_2 = {"name": "Chocolate", "price": 6.32}
product_3 = {"name": "Pasta", "price": 2.31}

# Add the products
my_cash_register.add_product(product_1)
my_cash_register.add_product(product_2, 3)
my_cash_register.add_product(product_3, 10)

my_cash_register.show_products()

# Remove a product
my_cash_register.remove_product("Pizza")
my_cash_register.show_products()

# Update the price of a product
my_cash_register.update_price("Pasta", 5.67)
my_cash_register.show_products()

# Print the subtotal, taxes, and total
my_cash_register.print_subtotal()
my_cash_register.print_taxes()
my_cash_register.print_total()

# Clear the purchase
my_cash_register.clear_purchase()
my_cash_register.show_products()
    
