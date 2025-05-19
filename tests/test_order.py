import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder(unittest.TestCase):

    def test_valid_order(self):
        customer = Customer("Ella")
        coffee = Coffee("Americano")
        order = Order(customer, coffee, 5.5)
        self.assertEqual(order.customer, customer)
        self.assertEqual(order.coffee, coffee)
        self.assertEqual(order.price, 5.5)

    def test_invalid_customer(self):
        coffee = Coffee("Latte")
        with self.assertRaises(TypeError):
            Order("NotACustomer", coffee, 4.5)

    def test_invalid_coffee(self):
        customer = Customer("Fred")
        with self.assertRaises(TypeError):
            Order(customer, "NotACoffee", 4.5)

    def test_invalid_price(self):
        customer = Customer("George")
        coffee = Coffee("Macchiato")
        with self.assertRaises(ValueError):
            Order(customer, coffee, 11.0)
        with self.assertRaises(ValueError):
            Order(customer, coffee, "free")

    def test_all_orders(self):
        Order._all_orders.clear()  # Reset before test
        customer = Customer("Hannah")
        coffee = Coffee("Mocha")
        Order(customer, coffee, 4.0)
        Order(customer, coffee, 5.0)
        self.assertEqual(len(Order.all()), 2)

if __name__ == '__main__':
    unittest.main()
