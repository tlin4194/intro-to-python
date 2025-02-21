# Appends names to a list for sorting
names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

# file is closed now
for name in sorted(names, reverse=True):
    print(f"hello, {name}")

print(names)
# Change Alice's name to Annie
names[0] = "Annie"

print(names)

with open("names.txt", "w") as file:
    for name in names:
        file.write(f"{name}\n")

# add David to the file

d = "David"
with open("names.txt", "a") as file:
    file.write(f"{d}\n")
