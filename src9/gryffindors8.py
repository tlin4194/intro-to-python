# Uses enumerate instead

students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
    print(i + 1, students[i])

for i, student in enumerate(students):
    print(i, student)
