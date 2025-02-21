# Passes a list


def main():
    yell(["This", "is", "CS50"])


def yell(words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)
    print("THIS", "IS", "CS50", sep="...")
    print(uppercased)


if __name__ == "__main__":
    main()
