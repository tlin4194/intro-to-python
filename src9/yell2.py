# Prints arbitrarily many args in uppercase


def main():
    yell("This", "is", "CS50", "Alice", "bob", ".....")


def yell(*words):
    print(words)
    print(type(words))
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)


if __name__ == "__main__":
    main()
