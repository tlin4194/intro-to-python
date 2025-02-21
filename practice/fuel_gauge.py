"""Fuel gauges indicate, often with fractions, just how much fuel is in a tank.
For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank
is 50% full, and 3/4 indicates that a tank is 75% full.

In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 10% or less remains, output E instead to indicate that the tank is essentially empty. And if 90% or more remains, output F instead to indicate that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.

Example:
Fraction: 3/4
75%
Fraction: 4/4
F
Fraction: 1/20
E
Fraction: bad/bad
Expecting X/Y where X and Y are integers!
Fraction: 1/0
Cannot divide by zero!
Fraction: 5/4
Fraction must be less than 1!
"""

f = input("Type a fraction in the format X/Y: ")
nums = f.split("/")
X = 0
Y = 0
new_f = 0.0
try:
    X = int(nums[0])
    Y = int(nums[1])

    if X > Y:
        raise ValueError("X cannot be greater than Y")
    if X < 0 or Y < 0:
        raise ValueError("X and Y must be positive ")
    print(nums)
    new_f = X/Y

except ValueError as err:
    print(f"ERROR: X and Y should be integers: {f}, {err}")
except ZeroDivisionError:
    print("Y cannot be 0! You can't divide a number by zero")
except Exception as err:
    print(err)

percentage = new_f * 100
if percentage <= 10:
    print("E")

elif percentage >= 90:
    print("F")

else:
    print(f"The percentage is {int(percentage)}%")


# try:
#     username = "asasldfjlsajdfl"
#     if len(username) > 10:
#         raise ValueError("username too long")
# except:
#     username = "default"
#     print("Username too long so I set it to the default")



# try:
#     print(3/4)
#     print(1/2)
#     print(x)
#     print(1/0) # bad one
#     print(4/5)
# except ZeroDivisionError:
#     print("Oops bad input!")
#     print("Try again...")
# # except NameError:
# #     print("x doesn't exist yet!")
# except Exception as err:
#     print(err)
