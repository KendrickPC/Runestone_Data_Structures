class Fraction:
    def __init__(self,top,bottom):
        def gcd(m, n):
            while m % n != 0:
                old_m = m
                old_n = n
                m = old_n
                n = old_m % old_n
            return n
        common = gcd(top,bottom)
        self.num = top/common
        self.den = bottom/common
    def __str__ (self):
        return str(self.num) + "/" + str(self.den)
    def get_num(self):
        return self.num
    def get_den(self):
        return self.den
    def __add__(self, other_fraction):
        new_num = self.num * other_fraction.den + self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        return Fraction(new_num, new_den)
    def __sub__(self, other_fraction):
        new_num = self.num * other_fraction.den - self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        return Fraction(new_num, new_den)
    def __mul__ (self, other_fraction):
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

a = Fraction(10,20)
b = Fraction(30,20)
print(a)
print("The numerator is",a.get_num())
print("The denominator is",a.get_den())
print("equality is",(a==b))
print("sum is",(a+b))
print("difference is",(a-b))
print("product is",(a*b))
print("division is",(a/b))




