# Reads a CSV file

with open("names.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} has {row[1]}")
