# # -*- coding: utf-8 -*-

# Programming Exercises:
# 1, Implement the simple methods getNum and getDen that will return
# the numerator and denominator of a fraction.


class Fraction:

    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den

testing_1 = Fraction(1, 2)
print(testing_1)

print(testing_1.getNum())
print(testing_1.getDen())
