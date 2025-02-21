"""Part 1 Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents
and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.
Implement a program that prompts the user to insert a coin, one at a time, each
time informing the user of the amount due. Once the user has inputted at least
50 cents, output how many cents in change the user is owed. Assume that the
user will only input integers, and ignore any integer that isn't an accepted
denomination.

I.e.
Amount Due: 50
Insert Coin: 25
Amount Due: 25
Insert Coin: 30
Coin Not Accepted!
Amount Due: 25
Insert Coin: 10
Amount Due: 15
Insert Coin: 25
Amount Due: 0
Change: 10


Part 2
Now we want to sell other things in the vending machine. You can sell whatever you like in the machine.

I.e.
coke: 100 cents
water: 50 cents
coffee: 200 cents
lemonade: 100 cents
chips: 150 cents
cookie: 225 cents
"""

vending_machine = {
    "coke": 50,
    "water": 50,
    "coffee": 200,
    "lemonade": 100,
    "chips": 150,
    "cookie": 225,
}


def main():
    while True:
        answer = input("Do you want to buy something?: (y/n) ")
        if answer == "y":
            choice = input("What would you like to buy?: ")
            if choice in vending_machine:
                cost = vending_machine[choice]
                print(f"The {choice} is {cost} cents")
                give_money(cost)
            else:
                print("You can't buy that.")
        if answer == "n":
            print("Goodbye")
            break


def give_money(cost):
    while cost > 0:
        coins = int(input("Insert coins: "))
        if coins == 25:
            cost -= 25
        elif coins == 10:
            cost -= 10
        elif coins == 5:
            cost -= 5
        else:
            print("Error! The machine only accepts 25, 10, or 5 cents at a time.")

        print(f"Amount due: {cost}")
    if cost < 0:
        print(f"Change: {cost * -1}")


main()


# Notes
# input()
# print()
