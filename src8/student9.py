# Defines class for a student


class Student:
    ...
    # this is a placeholder, but we can still use Student as is!


def main():
    student = get_student()
    print(student)
    print(type(student))
    print(f"{student.name} from {student.house}")


def get_student():
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    return student


if __name__ == "__main__":
    main()
