# Adds __init__


class Student:
    # creating new student -> constructor
    def __init__(self, arg_name, arg_house):
        self.name = arg_name
        self.house = arg_house


def main():
    student = get_student()
    print(f"{student.name} from {student.house}")


def get_student():
    input_name = input("Name: ")
    input_house = input("House: ")
    student = Student(arg_name=input_name, arg_house=input_house)
    return student


if __name__ == "__main__":
    main()
