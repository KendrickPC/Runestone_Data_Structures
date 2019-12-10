# 4.8. Converting Decimal Numbers to Binary Numbers

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


# Divide by 2 Function
def divideBy2(decNumber):
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2

    binString = ""
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())

    return binString

print("\nDivide By 2:")
print(divideBy2(42))


# Base Converter Function
def baseConverter(decNumber, base):
    digits = "0123456789ABCDEF"

    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base

    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]

    return newString

print("\nBase Converter:")
print(baseConverter(25, 2))
print(baseConverter(25, 16))



# Q-1: What is value of 25 expressed as an octal number?
print("\nValue of 25 expressed as an octal:")
print(baseConverter(25, 8))

# Q-2: What is value of 256 expressed as a hexidecimal number?
# Hexidecimal = 16
print("\nValue of 256 expressed as a hexidecimal:")
print(baseConverter(256, 16))

# Q-3: What is value of 26 expressed in base 26?
print("\nValue of 26 expressed in base 26:")
print(baseConverter(26, 26))







