"""Class Inheritance and Overriding Magic Methods Refer to area_of_shape.py for
area and input functions.

Task:
1. Create the classes Circle(), Rectangle(), and Triangle(). I've created a class Shape() for you, all three of your shapes will have this as the parent class.
2. All shapes will override the parent class method input_dimensions(). This function will be a class method, and it handles 3 things:
    A) Asks for user input on the width/length/radius (any relevant shape dimensions)
    B) Check user input to make sure inputs are valid, otherwise throw a ValueError()
    C) Return an instance of your shape with the inputted dimensions as init arguments.
    D) REMEMBER: class methods don't need an instance to be called! i.e. I don't need to create a Shape to call input_dimensions()
3. All shapes will override the parent class method get_area().
    A) return the area of that shape
4. All shapes will override the __str__ method:
    B) return the shape name and all of its dimensions.
5. Implement the __eq__, __lt__, and __gt__ functions in Shape().
"""
import math


class Shape():
    def __init__(self):
        self.area = self.get_area()

    def __str__(self):
        raise NotImplementedError("Must override __str__()")
        # you're going to override this method in the child classes so we can leave this empty

    def get_area(self):
        """Returns area of shape."""
        raise NotImplementedError("Must override get_area()")
        # override this method too

    def __eq__(self, other):
        # YOUR CODE HERE: return a Boolean for if areas for self and other are equal
        return self.area == other.area

    def __lt__(self, other):
        # YOUR CODE HERE: return a Boolean for if area for self is less than area for other shape
        return self.area < other.area

    def __gt__(self, other):
        # YOUR CODE HERE: return a Boolean for if area for self is greater than area for other shape
        return self.area > other.area

    @classmethod
    def input_dimensions(cls):
        """Ask for user input to set dimensions.

        Class methods can be called without an instance, so they're
        useful for constructors.
        """
        raise NotImplementedError("Must override input_dimensions()")
        # override this method too

###### ADD YOUR CLASSES HERE #####


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__()

    def __str__(self):
        return f"Circle with radius {self.radius}"

    @classmethod
    def input_dimensions(cls):
        radius = float(input("What is the radius? "))
        if radius <= 0:
            raise ValueError("Radius must be greater than zero.")
        return cls(radius)

    def get_area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length
        super().__init__()

    def __str__(self):
        return f"Rectangle with width {self.width} and length {self.length}"

    @classmethod
    def input_dimensions(cls):
        width = float(input("What is the width? "))
        length = float(input("What is the length? "))
        if width <= 0 or length <= 0:
            raise ValueError("Width and length must be greater than zero.")
        return cls(width, length)

    def get_area(self):
        return self.width * self.length


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
        super().__init__()

    @classmethod
    def input_dimensions(cls):
        base = float(input("What is the base? "))
        height = float(input("What is the height? "))
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be greater than zero.")
        return cls(base, height)

    def __str__(self):
        return f"Triangle with base {self.base} and height {self.height}"

    def get_area(self):
        return 0.5 * self.base * self.height


def main():
    # test your code by creating different shapes
    s = Square(10)
    print(s)
    print(s.area)

    c = Circle.input_dimensions()
    print(c)
    print(c.area)
    print(c == s)
    print(c < s)
    print(c > s)

    shapes = []
    shapes.append(Circle.input_dimensions())
    shapes.append(Rectangle.input_dimensions())
    shapes.append(Triangle.input_dimensions())

    for shape in shapes:
        print(shape)
        print(f"Area: {shape.area}")

        print(shape == shapes[0])
        print(shape < shapes[0])
        print(shape > shapes[0])

    print(shapes[1] == shapes[2])


if __name__ == "__main__":
    main()


class Square(Shape):
    """This is an example shape."""

    def __init__(self, side):
        self.side = side
        super().__init__()

    def __str__(self):
        return f"Square with side {self.side}"

    def get_area(self):
        return self.side * self.side

    @classmethod
    def input_dimensions(cls):
        pass
