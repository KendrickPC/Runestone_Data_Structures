# -*- coding: utf-8 -*-

# Modify the constructor for the fraction class so that it checks to make
# sure that the numerator and denominator are both integers. If either is
# not an integer the constructor should raise an exception.

# -*- coding: utf-8 -*-

# Implement the remaining relational operators 
# (__gt__, __ge__, __lt__, __le__, and __ne__)

from __future__ import division

class Fraction:

    def __init__(self, top, bottom):

        def gcd(m, n):
            while n:
                m, n = n, m % n
            return m
        common = gcd(top, bottom)
        self.num = int(top / common)
        self.den = int(bottom / common)

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, other_fraction):
        new_num = self.num * other_fraction.den + self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        return int(Fraction(new_num, new_den))

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

    def __eq__(self, other):
        first_num = self.num * other.den    
        second_num = other.num * self.den
        return first_num == second_num

    def __gt__(self, other_fraction):
        first_num = self.num * other_fraction.den
        second_num = other_fraction.num * self.den
        return first_num > second_num

    def __ge__(self, other_fraction):
        first_num = self.num * other_fraction.den
        second_num = other_fraction.num * self.den
        return first_num >= second_num

    def __lt__(self, other_fraction):
        first_num = self.num * other_fraction.den
        second_num = other_fraction.num * self.den
        return first_num < second_num

    def __le__(self, other_fraction):
        first_num = self.num * other_fraction.den
        second_num = other_fraction.num * self.den
        return first_num <= second_num

    def __ne__(self, other_fraction):
        first_num = self.num * other_fraction.den
        second_num = other_fraction.num * self.den
        return first_num != second_num

a = Fraction(1, 2)
b = Fraction(2, 3)
c = Fraction(25, 55)
d = Fraction(25, 55)


print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)

# print(a > b)
# print(c >= d)
# print(c < d)
# print(c <= d)

# print(c == d)
# print(c != d)
