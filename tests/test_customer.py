import unittest
from customer import Customer
from coffee import Coffee
from order import Order


class TestCustomer(unittest.TestCase):

    def test_valid_name(self):
        customer = Customer("Alice")
        self.assertEqual(customer.name, "Alice")

    def test_invalid_name_length(self):
        with self.assertRaises(ValueError):
            Customer("ThisIsAReallyLongName")

    def test_invalid_name_type(self):
        with self.assertRaises(ValueError):
            Customer(123)

    def test_orders_and_coffees(self):
        customer = Customer("Bob")
        coffee1 = Coffee("Latte")
        coffee2 = Coffee("Mocha")
        Order(customer, coffee1, 5.5)
        Order(customer, coffee2, 6.5)
        self.assertEqual(len(customer.orders()), 2)
        self.assertEqual(set(customer.coffees()), {coffee1, coffee2})

    def test_most_aficionado(self):
        customer1 = Customer("Sam")
        customer2 = Customer("Anna")
        coffee = Coffee("Espresso")
        Order(customer1, coffee, 3.0)
        Order(customer2, coffee, 5.0)
        self.assertEqual(Customer.most_aficionado(coffee), customer2)

if __name__ == '__main__':
    unittest.main()
