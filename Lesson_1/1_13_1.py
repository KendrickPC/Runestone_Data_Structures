# # -*- coding: utf-8 -*-
# Euclid’s Algorithm

# Finding the greatest common denominator

# def greatest_common_denominator(top, bottom):
#     while top % bottom != 0:
#         old_top = top
#         old_bottom = bottom

#         top = old_bottom
#         bottom = old_top % old_bottom
#     return bottom

# # Returns the greatest common denominator of two integers
# print(greatest_common_denominator(25, 95))


def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n

class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    def show(self):
        print(self.num,"/",self.den)
    
    # Addition method for fractions
    def __add__(self, otherfraction):
        newnum = self.num * otherfraction.den + \
                 self.den * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)
    
    # Subtraction method for fractions.
    def __sub__(self, otherfraction):
        newnum = self.num * otherfraction.den - \
                 self.den * otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)
        if newnum == 0:
            return 0
        return Fraction(newnum // common, newden // common)
    
    # Multiplication method for fractions.
    def __mul__(self, other):
        newnum = self.num * other.num
        newden = self.den * other.den
        common = gcd(newnum, newden)
        return Fraction(newnum // common, newden // common)

    # Division method for fractions.
    def __truediv__(self, other):
        newnum = self.num * other.den
        newden = self.den * other.num
        common - gcd(newnum, newden)
        return Fraction(newnum // common, newden //common)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
        return firstnum == secondnum

x = Fraction(4,3)
y = Fraction(2,6)

# Testing addition method.
print(x + y)
# Testing subtraction method.
print(x - y)
# Testing multiplication method.
print(x * y)

# Testing equality method.
print(x == y)
