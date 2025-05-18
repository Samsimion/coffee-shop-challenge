from customer import Customer
from coffee import Coffee
from order import Order

print("===== Customer Tests =====")
try:
    c1 = Customer("Samuel")
    print("PASS: Customer created →", c1.name)
except Exception as e:
    print("FAIL:", e)

try:
    c2 = Customer("A" * 20)
except ValueError as e:
    print("PASS: Name too long →", e)

try:
    c3 = Customer(123)
except ValueError as e:
    print("PASS: Name not a string →", e)


print("\n===== Coffee Tests =====")
try:
    coffee1 = Coffee("Latte")
    print("PASS: Coffee created →", coffee1.name)
except Exception as e:
    print("FAIL:", e)

try:
    coffee2 = Coffee("AB")
except ValueError as e:
    print("PASS: Coffee name too short →", e)

try:
    coffee1.name = "Espresso"
except AttributeError as e:
    print("PASS: Coffee name is immutable →", e)


print("\n===== Order Tests =====")
try:
    order1 = Order(c1, coffee1, 5.5)
    print(f"PASS: Order created → Customer: {order1.customer.name}, Coffee: {order1.coffee.name}, Price: {order1.price}")
except Exception as e:
    print("FAIL:", e)

try:
    order2 = Order("NotACustomer", coffee1, 5.5)
except TypeError as e:
    print("PASS: Invalid customer →", e)

try:
    order3 = Order(c1, "NotACoffee", 5.5)
except TypeError as e:
    print("PASS: Invalid coffee →", e)

try:
    order4 = Order(c1, coffee1, 15)
except ValueError as e:
    print("PASS: Price out of range →", e)

try:
    order5 = Order(c1, coffee1, 5)
except ValueError as e:
    print("PASS: Price is not a float →", e)
