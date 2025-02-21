"""Let's revisit the fibonacci function.

If I'm calling the function 100 times with different inputs, I have to recalculate the fibonacci from scratch (n=1) until n every time.
How can we make this a little more efficient?
Hint: If I'm calculating fib(8), I need fib(7), fib(6). If I already calculated those before and saved them somewhere, I can just use those directly instead of summing all the way up from 0 and 1.
Hint 2: What datatype would be good for storing calculated answers? Dictionaries, or lists.
"""


def main():
    tests = [1, 2, 0, 3, 5, 10, 10, 4, 7, 8]
    for test in tests:
        print(fib(test))
    print(saved_nums)


# Dictionary to store already computed Fibonacci numbers
# Start with the first two Fibonacci numbers
saved_nums = {1: 0, 2: 1}
# Global variable


def fib(n):
    # Just return the nth number in fibonacci sequence
    # i.e. If n = 7, return 8. If it's a bad input, return None.
    if n in saved_nums:
        return saved_nums[n]
    elif n <= 0:
        return None  # Where n is negative or zero
    else:
        for i in range(3, n + 1):
            saved_nums[i] = saved_nums[i - 1] + saved_nums[i - 2]
        # not sure if its instead : return saved_nums[n-1]
        return saved_nums[n]


main()
