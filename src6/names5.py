# Reads from a file

with open("names.txt", "r") as file:
    lines = file.readlines()
    print(type(lines))

for line in lines:
    print("hello,", line.rstrip())
