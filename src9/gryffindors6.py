# Uses dictionary comprehension instead

students = ["Hermione", "Harry", "Ron"]

gryffindors1 = [{"name": student, "house": "Gryffindor"}
                for student in students]
gryffindors2 = {student: "Gryffindor" for student in students}

print(gryffindors1)
print(gryffindors2)
