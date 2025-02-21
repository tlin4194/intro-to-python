# Filters by house using list comprehension

students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

gryffindors = [student["name"]
               for student in students if student["house"] == "Gryffindor"]

print([student["name"] for student in students if student["name"][0] == "H"])

for gryffindor in sorted(gryffindors):
    print(gryffindor)
