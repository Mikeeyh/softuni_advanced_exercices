number_of_students = int(input())

students = {}

for _ in range(number_of_students):
    name, grade = input().split()

    if name not in students:
        students[name] = []
    students[name].append(float(grade))

for student_name, grades in students.items():
    formatted_grades = ' '.join([f"{grade:.2f}" for grade in grades])
    print(f"{student_name} -> {formatted_grades} (avg: {(sum(grades) / len(grades)):.2f}")


# OR ----------------------------------------------------------------

number_of_students = int(input())

students = {}

for student in range(number_of_students):
    student_name, grade = input().split()

    if student_name not in students:
        students[student_name] = []
    students[student_name].append(float(grade))

for key, value in students.items():
    average_grade = sum(value) / len(value)
    formatted_grades = " ".join([f"{grade:.2f}" for grade in value])
    print(f'{key} -> {formatted_grades} (avg: {average_grade:.2f})')

print(students)

# 7
# Peter 5.20
# Mark 5.50
# Peter 3.20
# Mark 2.50
# Alex 2.00
# Mark 3.46
# Alex 3.00