#!/user/bin/python3
class ShoppingBag():
    def __init__(self):
        self.bag = {}

    def add_item(self, name, quantity):
        self.bag[name] = quantity

    def print_items(self):
        print(str(self.bag))

    def __add__(self, other):
        for name in other.bag:
            if name in self.bag:
                self.bag[name] = self.bag[name] + other.bag[name]
            else:
                self.bag[name] = other.bag[name]
        return self

    def __sub__(self, other):
        for name in other.bag:
            if name in self.bag:
                cur_items = self.bag[name]
                other_items = other.bag[name]

                if cur_items > other_items:
                    self.bag[name] = self.bag[name] - other.bag[name]
                else:
                    self.bag.pop(name)

        return self


my_bag = ShoppingBag()
other_bag = ShoppingBag()

my_bag.add_item("Bananas", 10)
my_bag.add_item("apples", 5)
other_bag.add_item("apples", 7)
combined_bag = my_bag + other_bag
combined_bag.print_items()
combined_bag = combined_bag - other_bag
combined_bag.print_items()

