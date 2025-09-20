number_of_people = int(input())
capacity_elevator = int(input())

courses = 0

while number_of_people != 0:
    number_of_people -= capacity_elevator
    courses += 1

    if number_of_people < 0:
        break

print(courses)