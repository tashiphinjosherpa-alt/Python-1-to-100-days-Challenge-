class ATM:
    def __init__(self):
        self.__balance = 1000

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient Balance")

    def showBalance(self):
        print("Balance:", self.__balance)

a = ATM()

a.deposit(500)
a.withdraw(200)
a.showBalance()