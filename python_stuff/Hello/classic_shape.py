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

    def print_shape_details(self):
        print("shape has {0} sides, perimeter {1}, area {2}".format(self.num_sides, self.perimeter(), self.area()))


class Square(Shape):
    def __init__(self, side_length, num_sides=4):
        self.num_sides = num_sides
        self.side_lengths = [side_length] * 4

    #def print_shape_details(self):
        #print("Shape has %d sides, perimeter %f, area %f" % (self.num_sides, self.perimeter(), self.area()))

    def area(self):
        return self.side_lengths[0] * self.side_lengths[0]


class Rectangle(Shape):
    def __init__(self, length, width, num_sides=4):
        self.num_sides = num_sides
        self.side_lengths = []
        self.side_lengths.append(length)
        self.side_lengths.append(width)
        self.side_lengths.append(length)
        self.side_lengths.append(width)

    def area(self):
        return self.side_lengths[0] * self.side_lengths[1]

some_shape = Shape(3, [2, 3, 4])
some_square = Square(3)
some_rectangle = Rectangle(3, 4)

some_shape.print_shape_details()
some_square.print_shape_details()
some_rectangle.print_shape_details()