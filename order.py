from customer import Customer
from coffee import Coffee

class Order:
    _all_orders = []
    def __init__(self,customer,coffee,price):
        if isinstance(customer, Customer):
            self._customer = customer
        else:
            raise TypeError("customer inafaa ikue kwa Customer instance")
        if isinstance(coffee,Coffee):
            self._coffee = coffee
        else:
            raise TypeError("coffee inafaa kukuaa kwa Coffee instance tafadhali")
        if isinstance(price, float) and 1.0 <= price <= 10.0:
            self._price = price
        else:
            raise ValueError("price must be a float between 1.0 and 10.0")
        
        Order._all_orders.append(self)
    
    @property
    def customer(self):
        return self._customer
    
    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price
    
    @classmethod
    def all(cls):
        return cls._all_orders
    
