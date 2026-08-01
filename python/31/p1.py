class BankAccount:
    def __init__(self):
        self.__balance = 0      # Private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient Balance")

    def show_balance(self):
        print("Balance:", self.__balance)


acc = BankAccount()

acc.deposit(1000)
acc.withdraw(300)

acc.show_balance()

# Trying to access directly
print(acc.__balance)

# print(acc._BankAccount__balance)

# Actually the fact is Python does not have strict encapsulation but yes to 
# 1. to accidental access
# 2. to show terminology 

# this is fine

