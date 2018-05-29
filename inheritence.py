"""
written by sourabh agrawal
This is simple program using the concepts of oops in python3
here i am implementing the simple program of finding area, volume using inheritance
"""


# !/usr/bin/python3
class Square(object):
    area = 0

    def getarea(self, l, w):
        return l * w

    def __init__(self, l, w):
        print("\nConstructor of square called")
        self.area = self.getarea(l, w)
        print("area is %d " % self.area)


class Volume(Square):
    h = 0

    def getvolume(self, ar):
        volume = ar * self.h

        print("volume is %d" % volume)

    def __init__(self, l, w, h):
        super().__init__(l, w)
        print("\nConstructor of volume called")
        self.h = h
        self.getvolume(self.area)


class Third(Volume, Square):
    """
    sfnuswgbuwbgiw
    """

    def __init__(self, l, w, h):
        print("\nconstructor of Third called")
        super().__init__(l, w, h)
        self.__doc__

    def __new__(cls, *args, **kwargs):
        print('New Method')
        return super().__new__(cls)


def main():
    l = int(input("Enter the length"))
    w = int(input("Enter the width"))
    h = int(input("Enter the height"))
    obj1 = Third(l, w, h)


if __name__ == '__main__': main()
