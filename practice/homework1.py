"""
1. Print "hello" 10 times in 5 different ways. Use for/while loops.

2. Fizzbuzz
* Write a function called fizzbuzz(), that takes in an integer as input. IF the integer is:
* divisible by 3, print "fizz"
* divisible by 5, print "buzz"
* divisible by both, print "fizzbuzz"

3. Given the height of a stack of boxes represented by "#", write a function box_stack() that prints the stack of boxes as a pyramid:

input: 3

  #  
 ### 
#####

input: 4

   #   
  ###  
 ##### 
#######
 
input: 5

    #
   ###
  #####
 #######
#########

"""


def main():
    # TEST YOUR CODE HERE
    # for f in [hello1, hello2, hello3, hello4, hello5]:
    #     f()
    #     print()
    assert fizzbuzz(3) == "fizz"
    assert fizzbuzz(5) == "buzz"
    assert fizzbuzz(15) == "fizzbuzz"
    assert fizzbuzz(6) == "fizz"
    assert fizzbuzz(10) == "buzz"
    assert fizzbuzz(30) == "fizzbuzz"

    # n = int(input("Enter an integer: "))
    # fizzbuzz(n)

    height = int(input("Enter a box stack height: "))
    box_stack(height)


def hello1():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for _ in nums:
        print("hello")
    # or
    print()
    for _ in range(10):
        print("hello")


def hello2():
    x = 1
    while x < 11:
        print("hello")
        x += 1


def hello3():
    y = 11
    while y > 1:
        print("hello")
        y -= 1


def hello4():
    h = "hello\n"
    print(h * 10)

    # or
    print()
    print("hello\n" * 10)


def hello5():
    print("hello")
    print("hello")
    print("hello")
    print("hello")
    print("hello")
    print("hello")
    print("hello")
    print("hello")
    print("hello")
    print("hello")


def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "fizzbuzz"
    if n % 3 == 0:
        return "fizz"
    if n % 5 == 0:
        return "buzz"
    else:
        return n


def box_stack(height):
    for i in range(height):
        spaces = height - i - 1
        # print(spaces)
        hashes = 2 * i + 1
        # print(hashes)
        print(" " * spaces + "#" * hashes)


main()
