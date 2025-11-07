students_and_grades = {}

number_of_iterations = int(input())

for _ in range(number_of_iterations):
    name = input()
    grade = float(input())
    if name not in students_and_grades.keys():
        students_and_grades[name] = []
    students_and_grades[name].append(grade)

for name in students_and_grades.keys():
    average_grade = sum(students_and_grades[name]) / len(students_and_grades[name])
    if average_grade >= 4.50:
        print(f"{name} -> {average_grade:.2f}")