sequence_of_numbers = list(map(int, input().split(", ")))

group_of_numbers = 10
list_of_numbers = []

while sequence_of_numbers :
    current_numbers_list = [num for num in sequence_of_numbers if int(num) <= group_of_numbers]
    print(f"Group of {group_of_numbers}'s: {current_numbers_list}")
    sequence_of_numbers = [number for number in sequence_of_numbers if number not in current_numbers_list]
    group_of_numbers += 10

