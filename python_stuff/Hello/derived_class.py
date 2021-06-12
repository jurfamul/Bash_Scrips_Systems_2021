#!/user/bin/python3
from functools import reduce


class Shape:
    def __init__(self, num_sides, side_lengths=[]):
        self.num_sides = num_sides
        self.side_lengths = side_lengths

    def perimeter(self):
        return reduce(lambda x, y: x + y, self.side_lengths)

    def area(self):
        pass # Not implemented

    def get_name(self):
        pass

    def print_shape_details(self):
        print("shape {0} has {1} sides: perimeter {2}, area {3}".format(self.get_name(), self.num_sides, self.perimeter(), self.area()))


class Rectangle(Shape):
    def __init__(self, length, width, num_sides=4):
        super(Rectangle, self).__init__(num_sides)
        self.side_lengths = []
        self.side_lengths.append(length)
        self.side_lengths.append(width)
        self.side_lengths.append(length)
        self.side_lengths.append(width)
        self.name = "Rectangle"

    def area(self):
        return self.side_lengths[0] * self.side_lengths[1]

    def get_name(self):
        return self.name


class Square(Rectangle):
    def __init__(self, side_length):
        super(Square, self).__init__(side_length, side_length)
        self.name = "Square"

    def get_name(self):
        return self.name


some_shape = Shape(3, [2, 3, 4])
some_rectangle = Rectangle(2, 3)
some_square = Square(3)

some_shape.print_shape_details()
some_rectangle.print_shape_details()
some_square.print_shape_details()
