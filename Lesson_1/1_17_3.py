# # -*- coding: utf-8 -*-

# Implement the remaining simple arithmetic operators
# (__sub__, __mul__, and __truediv__).

from __future__ import division

class Fraction:

    def __init__(self, top, bottom):

        def gcd(m, n):
            while n:
                m, n = n, m % n
            return m
        common = gcd(top, bottom)
        self.num = top / common
        self.den = bottom / common

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, other_fraction):
        new_num = self.num * other_fraction.den + self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        return Fraction(new_num, new_den)

    def __sub__(self, other_fraction):
        new_num = self.num * other_fraction.den - self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        return Fraction(new_num, new_den)

    def __mul__(self, other_fraction):
        new_num = self.num * other_fraction.num
        new_den = self.den * other_fraction.den
        return Fraction(new_num, new_den)

    def __truediv__(self, other_fraction):
        new_num = self.num * other_fraction.den
        new_den = self.den * other_fraction.num
        return Fraction(new_num, new_den)

a = Fraction(1, 2)
b = Fraction(2, 3)

print(a - b)
print(a * b)
print(a / b)
