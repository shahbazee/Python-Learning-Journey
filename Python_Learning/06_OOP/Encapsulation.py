
class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance.")

    def get_balance(self):
        return self.__balance


account = BankAccount("Ali", 5000)

account.deposit(1000)
account.withdraw(2000)

print("Current Balance:", account.get_balance())

# print(account.__balance)   # AttributeError