class Bank:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient Balance")

    def show_balance(self):
        print("Balance =", self.__balance)

b = Bank()

b.deposit(5000)
b.withdraw(1000)
b.show_balance()