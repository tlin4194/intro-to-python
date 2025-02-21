# Unpacks a list

with open("names.csv") as file:
    for line in file:
        name, email = line.rstrip().split(",")
        print(f"{name} 's email is {email}")
