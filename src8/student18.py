# Adds @property for house


class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Invalid name")
        self.name = name
        self._house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    # Getter function -> get this attribute
    @property  # decorator
    def house(self):
        return self._house

    # Setter function -> set this attribute to something
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house


def main():
    student = get_student()
    student.house = "Something random"
    print(student.house)
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
