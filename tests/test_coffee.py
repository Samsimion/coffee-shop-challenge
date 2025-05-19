import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCoffee(unittest.TestCase):

    def test_valid_name(self):
        coffee = Coffee("Latte")
        self.assertEqual(coffee.name, "Latte")

    def test_invalid_name(self):
        with self.assertRaises(ValueError):
            Coffee("Hi")

    def test_name_immutable(self):
        coffee = Coffee("Mocha")
        with self.assertRaises(AttributeError):
            coffee.name = "NewName"

    def test_orders_and_customers(self):
        customer = Customer("Chris")
        coffee = Coffee("Cappuccino")
        Order(customer, coffee, 4.0)
        self.assertEqual(len(coffee.orders()), 1)
        self.assertEqual(coffee.customers(), [customer])

    def test_average_price(self):
        customer = Customer("Dee")
        coffee = Coffee("Flat White")
        Order(customer, coffee, 4.0)
        Order(customer, coffee, 6.0)
        self.assertEqual(coffee.average_price(), 5.0)

if __name__ == '__main__':
    unittest.main()
