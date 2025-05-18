from order import Order

class Customer:
    def __init__(self,name):
        self.name = name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        if isinstance(name, str) and 1<= len(name) <=15:
            self._name = name
        else:
            raise ValueError("Name must be a string between 1 and 15 characters.")
        
    def orders(self):
        return [order for order in Order.all() if order.customer == self]
    
    def coffees(self):
        return list({order.coffee for order in self.orders()})
    
    def num_orders(self):
        return len(self.orders())
    
    @classmethod
    def most_aficionado(cls, coffee):
        customers = set(order.customer for order in Order.all() if order.coffee == coffee)
        if not customers:
            return None

        return max(customers, key=lambda customer: sum(
            order.price for order in Order.all()
            if order.customer == customer and order.coffee == coffee
        ), default=None)


