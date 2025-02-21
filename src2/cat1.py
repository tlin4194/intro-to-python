# Demonstrates a while loop, counting down

# i = 3
# while i != 0:
#     print("meow")
#     i = i - 1


names = ["Alice", "Bob", "Cathy"]

i = 3
while i != 0:
    names[i-1] += " Smith"
    i = i - 1

print(names)
