#!/usr/bin/env python3.8
"""
Find The Torsional Angle Jerod Gawne, 2020.07.29 <https://github.com/jerodg/hackerrank>
"""
from math import acos, degrees


class Points(object):

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        return Points((self.x - no.x), (self.y - no.y), (self.z - no.z))

    def dot(self, no):
        return (self.x * no.x) + (self.y * no.y) + (self.z * no.z)

    def cross(self, no):
        return Points((self.y * no.z - self.z * no.y), (self.z * no.x - self.x * no.z), (self.x * no.y - self.y * no.x))

    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)


def main():
    points = [list(map(float, input().split())) for _ in range(4)]

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = acos(x.dot(y) / (x.absolute() * y.absolute()))

    print(f'{degrees(angle):.2f}')


if __name__ == '__main__':
    main()
