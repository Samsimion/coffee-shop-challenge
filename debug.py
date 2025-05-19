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


print("\n===== Relationship and Method Tests =====")

# Setup objects
c1 = Customer("Samuel")
c2 = Customer("Anna")
coffee1 = Coffee("Latte")
coffee2 = Coffee("Espresso")

# Create orders
order1 = Order(c1, coffee1, 5.0)
order2 = Order(c1, coffee1, 6.0)
order3 = Order(c1, coffee2, 7.0)
order4 = Order(c2, coffee1, 5.5)

# Test Customer.orders()
print("Customer.orders() returns correct orders:")
print("Expected 3 orders for Samuel, got:", len(c1.orders()))
print("Expected 1 order for Anna, got:", len(c2.orders()))

# Test Customer.coffees()
print("Customer.coffees() returns unique coffees:")
print("Expected 2 unique coffees for Samuel, got:", len(c1.coffees()))
print("Expected 1 unique coffee for Anna, got:", len(c2.coffees()))

# Test Coffee.orders()
print("Coffee.orders() returns correct orders:")
print("Expected 3 orders for Latte, got:", len(coffee1.orders()))
print("Expected 1 order for Espresso, got:", len(coffee2.orders()))

# Test Coffee.customers()
print("Coffee.customers() returns unique customers:")
print("Expected 2 unique customers for Latte, got:", len(coffee1.customers()))
print("Expected 1 unique customer for Espresso, got:", len(coffee2.customers()))

# Test Coffee.num_orders()
print("Coffee.num_orders() returns correct count:")
print("Expected 3 for Latte, got:", coffee1.num_orders())

# Test Coffee.average_price()
print("Coffee.average_price() calculates average price correctly:")
expected_avg_latte = (5.0 + 6.0 + 5.5) / 3
print(f"Expected {expected_avg_latte:.2f} for Latte, got: {coffee1.average_price():.2f}")

# Test Customer.most_aficionado()
print("Customer.most_aficionado() returns the customer who spent most on a coffee:")
most_aff_latte = Customer.most_aficionado(coffee1)
print("Expected Samuel or Anna (who spent more?), got:", most_aff_latte.name)

# Edge case: no orders
print("Edge case: Coffee with no orders returns 0.0 average price:")
coffee3 = Coffee("Mocha")
print("Expected 0.0, got:", coffee3.average_price())

print("Edge case: Customer with no orders returns empty list:")
c3 = Customer("Empty")
print("Expected 0 orders, got:", len(c3.orders()))

# Test Order.all()
print("Order.all() returns all orders created:")
print("Expected at least 4, got:", len(Order.all()))
