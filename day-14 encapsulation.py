class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance   # private variable

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount
        return self.__balance


b = BankAccount("sandhiya", 200.0)

print(b.deposit(100))
print(b.balance)
    
