# 2.1.1. A Basic implementation of the MSDie class

"""
Lets start with a really simple implementation of the MSDie class, and we’ll
improve it one step at a time. We want to make our die a bit flexible so the
constructor will allow us to specify the number of sides.
"""

# Importing random module.
import random

"""
Creating a multi-sided die.
Instance variables include the following:
    
    current_value
    num_sides

"""

class MSDie:
    def __init__(self, num_sides):
        self.num_sides = num_sides
        self.current_value = self.roll()

    def roll(self):
        self.current_value = random.randrange(1, self.num_sides + 1)
        return self.current_value

my_die = MSDie(6)
for i in range(5):
    print(my_die, my_die.current_value)
    my_die.roll()

d_list = [MSDie(6), MSDie(20)]
print(d_list)