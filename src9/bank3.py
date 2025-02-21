# Uses class

# global variables
# constant - variable we're not going to change
# MIN_BALANCE = -50
# MAX_BALANCE = 500


class Account:
    # class variable: applies to every instance of this class
    MIN_BALANCE = -50
    MAX_BALANCE = 500

    def __init__(self):
        self._balance = 0  # instance variable: only for one instance

    @property
    def balance(self):
        return self._balance

    def deposit(self, n):
        if self._balance + n < self.MAX_BALANCE:
            self._balance += n

    def withdraw(self, n):
        if self._balance - n > self.MIN_BALANCE:
            self._balance -= n


def main():
    account1 = Account()
    print("Balance1:", account1.balance)
    account1.deposit(100)
    print("Balance1:", account1.balance)
    account1.deposit(500)
    print("Balance1:", account1.balance)
    account1.withdraw(50)
    print("Balance1:", account1.balance)

    account2 = Account()
    account2.MAX_BALANCE = 600
    print("Balance2:", account2.balance)
    account2.deposit(550)
    print("Balance2:", account2.balance)
    account2.deposit(499)
    print("Balance2:", account2.balance)
    print(account2.MAX_BALANCE)

    account3 = Account()
    print("Balance3:", account3.balance)
    print(account3.MAX_BALANCE)
    account3.deposit(550)
    print("Balance3:", account3.balance)


if __name__ == "__main__":
    main()
