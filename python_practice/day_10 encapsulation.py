class bank:
    def __init__(self):
        self._balance=0.0
       
    @property
    def balance(self):
        return self._balance
    def deposit(self,amount):
        self.amount=amount
        if(amount<=0):
            raise ValueError("Amount should be greater than 0")
        self._balance+=amount
    def withdraw(self,amount):
        self.amount=amount
        if(amount<=0):
            raise ValueError("Withdraw amount should be greater than 0")
        if(amount>self._balance):
            raise ValueError("Insufficiant funds")
        self._balance-=amount
account=bank()
print(account.balance)
account.deposit(1000)
print(account.balance)
account.withdraw(900)
print(account.balance)


