# Demonstrates a function that returns a bool


def main():
    x = int(input("What's x? "))
    ans = is_even(x)
    print(f"Is {x} even? {ans}")


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


main()
