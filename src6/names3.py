# Appends to a file

name = input("What's your name? ")
file = open("names.txt", "a")
print(type(file))
file.write(f"{name}")
file.close()
