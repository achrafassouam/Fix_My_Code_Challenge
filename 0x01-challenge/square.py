#!/usr/bin/python3
""" Square module """


class Square():
    """ Square class """

    def __init__(self, side=0):
        """ Init for Square class """
        self.side = side

    def area_of_my_square(self):
        """ Area of the square """
        return self.side * self.side

    def perimeter_of_my_square(self):
        """ Perimeter of the square """
        return self.side * 4

    def __str__(self):
        """ str representation of square """
        return "Square with side: {}".format(self.side)


if __name__ == "__main__":
    """ Square instance """
    s = Square(side=12)
    print(s)
    print("Area:", s.area_of_my_square())
    print("Perimeter:", s.perimeter_of_my_square())
