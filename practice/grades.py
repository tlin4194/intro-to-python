"""
Write a function grades_summary(students) that takes a list of lists as input, where each inner list represents the grades of a single student.
The function should return a list of tuples, where each tuple contains:
The average grade (rounded to two decimal places)
The highest grade
The lowest grade
If a student has no grades (an empty list), return (0, 0, 0) for that student."""


def main():
    students = [[90, 80, 85, 70, 95], [78, 88, 92], [85, 75], [], [100, 95, 90, 80, 70]]

    result = get_grades_summary(students)
    print(result)

    # [(avg, max, min), (avg2, max2, min2)....]


def get_grades_summary(students):
    # create variables we need
    grades_summary = []

    # implement my logic
    for student in students:
        if len(student) == 0:  # if student doesn't have grades
            grades_summary.append((0, 0, 0))
        else:  # student has grades, then do the math
            average = sum(student) / len(student)
            highest = max(student)
            lowest = min(student)
            grades_per_student = (average, highest, lowest)
            grades_summary.append(grades_per_student)
    return grades_summary


main()
