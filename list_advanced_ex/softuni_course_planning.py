def add(course_list:list, command:list) -> list:
    lesson_title = command[1]
    if lesson_title not in course_list:
        course_list.append(lesson_title)
    return course_list

def ins(course_list:list, command:list) -> list:
    lesson_title, index = command[1], int(command[2])
    if lesson_title not in course_list:
        course_list.insert(index, lesson_title)
    return course_list

def rem(course_list:list, command:list) -> list:
    lesson_title = command[1]
    if lesson_title in course_list:
        course_list.remove(lesson_title)
    if f"{lesson_title}-Exercise" in course_list:
        for index in range(len(course_list)):
            if course_list[index] == f"{lesson_title}-Exercise":
                course_list.remove(index)
    return course_list

def swap(course_list:list, command:list) -> list:
    lesson_title_for_swap, lesson_title_to_be_swapped = command[1], command[2]
    first_swapped_index = 0
    second_swapped_index = 0

    if lesson_title_for_swap in course_list and lesson_title_to_be_swapped in course_list:
        for index in range(len(course_list)):
            if course_list[index] == lesson_title_for_swap:
                course_list[index] = lesson_title_to_be_swapped
                first_swapped_index = index
            elif course_list[index] == lesson_title_to_be_swapped:
                course_list[index] = lesson_title_for_swap
                second_swapped_index = index

    if f"{lesson_title_for_swap}-Exercise" in course_list:
        course_list.pop(first_swapped_index + 1)
        course_list.insert(second_swapped_index + 1, f"{lesson_title_for_swap}-Exercise")

    if f"{lesson_title_to_be_swapped}-Exercise" in course_list:
        course_list.pop(second_swapped_index + 1)
        course_list.insert(first_swapped_index + 1, f"{lesson_title_to_be_swapped}-Exercise")
    return course_list

def exercise(course_list:list, command:list) -> list:
    lesson_title = command[1]
    if lesson_title in course_list:
        for index in range(len(course_list)):
            if course_list[index] == lesson_title:
                course_list.insert((index + 1),f"{lesson_title}-Exercise")
    else:
        course_list.append(lesson_title)
        course_list.append(f"{lesson_title}-Exercise")
    return course_list


initial_schedule = input().split(", ")

courses_row = 0

while True:
    command = input().split(":")
    courses_row += 1

    if command[0] == "course start":
        break

    elif command[0] == "Add":
        initial_schedule = add(initial_schedule, command)

    elif command[0] == "Insert":
        initial_schedule = ins(initial_schedule, command)

    elif command[0] == "Remove":
        initial_schedule = rem(initial_schedule, command)

    elif command[0] == "Swap":
        initial_schedule = swap(initial_schedule, command)

    elif command[0] == "Exercise":
        initial_schedule = exercise(initial_schedule, command)

for index in range(len(initial_schedule)):
    print(f"{index + 1}.{initial_schedule[index]}")