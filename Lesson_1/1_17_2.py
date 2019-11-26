# # -*- coding: utf-8 -*-

'''
Programming Exercises:
2. In many ways it would be better if all fractions were maintained
in lowest terms right from the start. Modify the constructor for
the Fraction class so that GCD is used to reduce fractions
immediately. Notice that this means the __add__ function no longer 
needs to reduce. Make the necessary modifications.
'''


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

a = Fraction(1, 2)
b = Fraction(2, 3)

print(a + b)