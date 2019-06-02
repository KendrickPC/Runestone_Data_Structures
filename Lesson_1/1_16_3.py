# -*- coding: utf-8 -*-

"""
Discussion Questions:
3. Construct a class hierarchy for different types of computers.
4. Using the classes provided in the chapter, interactively construct
a circuit and test it.
"""


class Computer:

    def __init__(self, cpu, brand_name, operating_system):
        self.cpu_name = cpu
        self.reference = brand_name
        self.os = operating_system

    def __str__(self):
        return "The computer's CPU uses " + self.cpu_name + ", " + \
               "the manufacturer is " + self.reference + ", " + \
               "and the operating system is " + self.os


class Laptop(Computer):
    
    def __init__(self, cpu, brand_name, operating_system):
        super().__init__(cpu, brand_name, operating_system)

    def __str__(self):
        return super().__str__()        


class Cell_Phone(Computer):
    
    def __init__(self, cpu, brand_name, operating_system):
        super().__init__(cpu, brand_name, operating_system)

    def __str__(self):
        return super().__str__()


class Desktop(Computer):
    def __init__(self, cpu, brand_name, operating_system):
        super().__init__(cpu, brand_name, operating_system)

    def __str__(self):
        return super().__str__()


macbook = Laptop('Intel', 'Apple', 'OSX')
iphone = Cell_Phone('A9', 'Apple', 'iOS')
mac_pro = Desktop('Intel', 'Apple', 'OSX')


print(macbook)
print(iphone)
print(mac_pro)