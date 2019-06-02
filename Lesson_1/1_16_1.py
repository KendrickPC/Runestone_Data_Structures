# -*- coding: utf-8 -*-

"""
Discussion Question:
1. Construct a class hierarchy for people on a college campus.
Include faculty, staff, and students. What do they have in common?
What distinguishes them from one another?
"""

# What they have in common is that they are all people.
# What distinguishes them from one another is their title.
# I added a nickname in there for fun.

class Person:

    def __init__(self, first, last, age):
        self.firstname = first
        self.lastname = last
        self.age = age

    def __str__(self):
        return self.firstname + " " + self.lastname + ", " + str(self.age)


class Professor(Person):
    
    def __init__(self, first, last, age, title, nickname):
        super().__init__(first, last, age)
        self.titlename = title
        self.aliasname = nickname

    def __str__(self):
        return super().__str__() + ", " + self.titlename + ", " + self.aliasname


class Staff(Person):

    def __init__(self, first, last, age, title, nickname):
        super().__init__(first, last, age)
        self.titlename = title
        self.aliasname = nickname

    def __str__(self):
        return super().__str__() + ", " + self.titlename + ", " + self.aliasname


class Student(Person):

    def __init__(self, first, last, age, title, nickname):
        super().__init__(first, last, age)
        self.titlename = title
        self.aliasname = nickname

    def __str__(self):
        return super().__str__() + ", " + self.titlename + ", " + self.aliasname

a = Person("Kenderson", "Chang", 37)
b = Professor("Ted", "Kaczynski", 77, "Professor", "Unabomber")
c = Staff("Will", "Hunting", 21, "Staff", "Good Will Hunting")
d = Student("Marty", "McFly", 21, "Student", "McFly")


print(a)
print(b)
print(c)
print(d)
