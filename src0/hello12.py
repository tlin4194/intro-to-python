# Demonstrates defining a main function


def main():
    name = input("What's your name? ")
    hello(name)
    hi(name)
    welcome(name)


def hello(to="world"):
    print("hello,", to)


def hi(to="world"):
    print("hi,", to)


def welcome(to="world"):
    print("welcome,", to)


main()
