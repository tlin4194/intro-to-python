"""
Fibonacci Sequence Printer
Write a Python function that takes an integer n as input and prints the first n numbers in the Fibonacci sequence.

i.e. n=7
0 1 1 2 3 5 8 13 21 34
"""


def main():
    fibonacci_sequence(10)


def fibonacci_sequence(n):
    if n <= 0:
        print("Bad input")
        return

    # 0 1 1 2 3 5 8
    #   F S N
    #     F S N

    counter = 0
    first = 0
    second = 1
    while counter < n:
        print(f"{first}", end=" ")
        nxt = first + second
        first = second
        second = nxt
        counter += 1
    print()


main()
