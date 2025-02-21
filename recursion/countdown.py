def countdown(n):
    """N is a positive number, print from n to zero."""
    while n >= 0:
        print(n)
        n -= 1


def countdown2(n):
    """Countdown but with recursion."""
    print(n)
    if n == 0:
        return             # Base case: Terminate recursion
    else:
        countdown(n - 1)   # Recursive call: moves closer to base case


def countdown3(n):
    """Simplified version of countdown2."""
    print(n)
    if n > 0:
        countdown(n - 1)
