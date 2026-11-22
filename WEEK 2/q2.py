class BankAccount: 
    def __init__(self, account_number, _balance=0): 
        self.account_number = account_number 
        self._balance = _balance
    def deposit(self, amount):
        self._balance += amount
        print("new balance is:", self._balance)
    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print("new balance is:", self._balance)
        else:
            print("insufficient funds")
b1 = BankAccount("A1")
b1.deposit(500)
b1.withdraw(200)
b1.withdraw(400)