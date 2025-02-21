# Adds wallets, storing total in new wallet


class Wallet:
    def __init__(self, pennies=0, nickels=0, dimes=0):
        self.pennies = pennies
        self.nickels = nickels
        self.dimes = dimes

    def __str__(self):
        return f"{self.pennies} pennies, {self.nickels} nickels, {self.dimes} dimes"


alice = Wallet(100, 50, 25)
print(alice)

bob = Wallet(25, 50, 100)
print(bob)

pennies = alice.pennies + bob.pennies
nickels = alice.nickels + bob.nickels
dimes = alice.dimes + bob.dimes

total = Wallet(pennies, nickels, dimes)
print(total)
