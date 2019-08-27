#!/usr/bin/env python3

from math import pi

class Circle():

    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self._diameter = value
        self.radius = value / 2

    @property
    def area(self):
        return (self.radius ** 2) * pi

    @classmethod
    def from_diameter(cls, value):
        diameter = value / 2
        return cls(diameter)

    def __str__(self):
        return 'Circle with radius: {:.6f}'.format(float(self.radius))

    def __repr__(self):
        return "Circle({})".format(self.radius)

    def __add__(self, other):
        return Circle(self.radius + other.radius)

    def __iadd__(self, other):
        if type(other) == int or type(other) == float:
            return Circle(self.radius + other)
        else:
            return Circle(self.radius + other.radius)

    def __imul__(self, other):
        return Circle(self.radius * other)

    def __mul__(self, other):
        return Circle(self.radius * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        return self.radius / other

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def sort(self, other):
        return self.radius < other.radius


class Sphere(Circle):

    @property
    def area(self):
        return 4 * pi * (self.radius ** 2)

    @property
    def volume(self):
        return 4/3 * pi * (self.radius ** 3)

    def __str__(self):
        return 'Sphere with radius: {:.6f}'.format(float(self.radius))

    def __repr__(self):
        return "Sphere({})".format(self.radius)
