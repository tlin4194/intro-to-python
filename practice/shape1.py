""""""
import math


def main():
    rectangle_or_circle = input(
        "Do you want to find the area of a rectangle or circle? (r/c) ").lower().strip()
    if rectangle_or_circle == "rectangle" or rectangle_or_circle == "r":
        prompt_rectangle()
    elif rectangle_or_circle == "circle" or rectangle_or_circle == "c":
        prompt_circle()


def prompt_rectangle():
    width = int(input("What is the width?"))
    length = int(input("What is the length?"))
    answer = get_area(l=length, w=width)
    print(f"The area of the rectangle is {answer}")


def prompt_circle():
    radius = float(input("What is the radius? "))
    answer_circle = circle_area(r=radius)
    print(f"The area of the circle is {answer_circle}")


def get_area(w, l):
    area = w * l
    return area


def circle_area(r):
    area = (math.pi) * pow(r, 2)
    return area


main()

# Tips
# print (math.pi)
# pow(base, exp)
