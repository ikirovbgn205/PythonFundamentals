students_and_courses = input()

students = {}

while ":" in students_and_courses:
    info = students_and_courses.split(":")
    name, identification, course = info[0], info[1], info[2]
    if course not in students:
        students[course] = {}
    students[course][identification] = name

    students_and_courses = input()

students_and_courses = " ".join(students_and_courses.split("_"))
for key, value in students.items():

    if key in students_and_courses:
        for name, identification in value.items():
            print(f"{identification} - {name}")