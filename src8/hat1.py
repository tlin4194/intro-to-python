# Implements sort() with a class method
# houses doesn't change between different instances of Hat, don't need to init it every time


import random


class Hat:
    # Class variables
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))


# don't need to create a hat to use sort()
Hat.sort("Harry")
