
class Coffee:
    def __init__(self,name):
         if isinstance(name, str) and len(name) >= 3:
             self._name = name
         else:
             raise ValueError("Name must be a string with at least 3 characters.")



    @property
    def name(self):
        return self._name
    
    def orders(self):
        from order import Order
        return [order for order in Order.all() if order.coffee == self]
    
    def customers(self):
         return list({order.customer for order in self.orders()})
    
    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        orders = self.orders()
        if orders:
            total = sum(order.price for order in orders)
            return total / len(orders)
        return 0.0

    