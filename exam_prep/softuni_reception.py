first_receptionist = int(input())
second_receptionist = int(input())
third_receptionist = int(input())

students_count = int(input())
hours = 0
students_per_hour = first_receptionist + second_receptionist + third_receptionist

while students_count > 0:
    hours += 1
    students_count -= students_per_hour
    if hours % 4 == 0:
        hours += 1
print(f"Time needed: {hours}h.")
