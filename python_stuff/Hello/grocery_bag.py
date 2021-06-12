#!/user/bin/python3
class ShoppingBag():
    def __init__(self):
        self.bag = {}

    def add_item(self, name, quantity):
        self.bag[name] = quantity

    def __add__(self, other):
        for x in other.bag:
            self.bag.update(x)

    def __sub__(self, other):
        for x in other.bag:

            self.pop()

