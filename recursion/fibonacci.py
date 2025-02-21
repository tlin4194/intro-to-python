# index:    0, 1, 2, 3, 4, 5, 6
# fib_nums: 0, 1, 1, 2, 3, 5, 8

def main():
    print(fibonacci_memo(6))


#### Part 1 ####
def fibonacci(n):
    """"Find the nth fibonacci number."""
    first = 0
    second = 1
    if n == 0:
        return first
    if n == 1:
        return second
    for _ in range(2, n+1):  # remember range stops before n+1, not at n+1
        nxt = first + second
        first = second
        second = nxt
    return second

#### Part 2 ####


def fibonacci_recursion(n):
    """Find the nth fibonacci number with recursion."""
    # Base case
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive Call
    else:
        prev = fibonacci_recursion(n-1)
        prevprev = fibonacci_recursion(n-2)
        return prev + prevprev

#### Part 3 ####


def fibonacci_recursion2(n):
    """"Find the nth fibonacci number with recursion, base case simplified."""
    print(n)
    # Base case
    if n <= 1:
        return n
    # Recursive Call
    else:
        return fibonacci_recursion2(n-1) + fibonacci_recursion2(n-2)


#### Part 4 ####

# Right now, to find fib(5), I have to call fib(4) + fib(3).
# To find that fib(4), I call fib(3) and fib(2). And so on....
# Recursive function calls look like this (each line is a function call):
#
#                          fib(5)
#                     /               \
#                fib(4)               fib(3)
#              /        \              /       \
#          fib(3)      fib(2)      fib(2)   fib(1)
#         /    \       /    \        /      \
#   fib(2)   fib(1)  fib(1) fib(0) fib(1) fib(0)
#   /     \
# fib(1) fib(0)

# 5, 4, 3, 2, 1, 0, 1, 2, 1, 0, 3, 2, 1, 0, 1

# How many times did I calulate fib(3)? fib(2)? fib(1)?

# This is super wasteful...what if I stored each fib num the first time we calculate it,
# instead of continuing the recursive calls?
# Note that fib(1) and fib(0) don't trigger recursive calls since they are base case.

# Now the function call tree looks like this:
# (* star means it's the first time we've calculated that number)
#
#                      fib(5)
#                     /      \
#                *fib(4)*     fib(3)
#               /        \
#          *fib(3)*       fib(2)
#          /    \
#    *fib(2)*   fib(1)
#    /     \
# fib(1) fib(0)


# list to store all the fibonacci numbers we've already calculated
fib_nums = [0, 1]


def fibonacci_memo(n):
    """Find the nth fibonacci number, but uses a table to store results."""
    print(n)
    if n >= len(fib_nums):   # never calculated this fib num before
        print("NEW NUM")
        new_fib = fibonacci_memo(n - 1) + fibonacci_memo(n - 2)
        fib_nums.append(new_fib)
    return fib_nums[n]


main()
