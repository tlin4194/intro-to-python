# Adds vaults via operator overloading


class Wallet:
    def __init__(self, pennies=0, nickels=0, dimes=0):
        self.pennies = pennies
        self.nickels = nickels
        self.dimes = dimes

    def __str__(self):
        return f"{self.pennies} pennies, {self.nickels} nickels, {self.dimes} dimes"

    def __add__(self, other):
        pennies = self.pennies + other.pennies
        nickels = self.nickels + other.nickels
        dimes = self.dimes + other.dimes
        return Wallet(pennies, nickels, dimes)


alice = Wallet(100, 50, 25)
print(alice)

bob = Wallet(25, 50, 100)
print(bob)

total = alice + bob
print(total)
