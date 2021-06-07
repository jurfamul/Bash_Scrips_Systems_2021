#!/user/bin/python3
import math
class triangle:
    def __init__(self, side1, side2, base):
        if base < side1 + side2 :
            self.side1 = side1
            self.side2 = side2
            self.base = base
        else:
            print("error: base, {0}, is greater than or equal to the sum of side1, {01}, and side2< {2}."
                  .format(base, side1, side2))

    def perimeter(self):
        return self.base + self.side1 + self.side2

    #def height(self):
