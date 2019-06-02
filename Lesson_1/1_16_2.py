# -*- coding: utf-8 -*-

"""
Discussion Questions:
2. Construct a class hierarchy for bank accounts.
"""


class BankAccount:

    def __init__(self, name, savings_account, checking_account, balance = 0.00):
        self.name = name
        self._balance = balance
        self._savings = savings_account
        self._checking = checking_account

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= amount

    @property
    def balance(self):
        """check the balance"""
        return self._balance

    def __repr__(self):
        return '{0.__class__.__name__}(name={0.name}, balance={0.balance})'.format(self)

    def __str__(self):
        return 'Bank account of {}, current balance: {}'.format(self.name, self.balance)


customer1 = BankAccount('Alex', 300, 150)
print(repr(customer1))
customer1.deposit(100)
customer1.withdraw(30)
print(customer1)
customer2 = BankAccount('Sam', 'savings', 'checking', 200)
print(customer2.balance)



