# Returns student as tuple, unpacking it


def main():
    my_name, my_house = get_student()
    print(f"{name} from {house}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house)  # returning a tuple


if __name__ == "__main__":
    main()
