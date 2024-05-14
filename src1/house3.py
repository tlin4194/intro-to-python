# Uses |

name = input("What's your name? ")

match name:
    case "Harry" or "Hermione" or "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
