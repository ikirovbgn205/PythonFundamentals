def shoot(some_targets_list:list, index:int, value:int) -> list:
    if index in range(len(some_targets_list)):
        some_targets_list[index] -= value
        if some_targets_list[index] <= 0:
            del some_targets_list[index]
    return some_targets_list

def add(some_targets_list:list, index:int, value:int)-> list:
    if index not in range(len(some_targets_list)):
        print("Invalid placement!")
    else:
        some_targets_list.insert(index, value)
    return some_targets_list

def strike(some_targets_list:list, index:int, value:int)-> list:
    before_strike = index - value
    after_strike = index + value
    if before_strike not in range(len(some_targets_list)) or (after_strike not in range(len(some_targets_list))):
        print("Strike missed!")
    else:
        some_targets_list = some_targets_list[:before_strike] + some_targets_list[after_strike + 1:]
    return some_targets_list


sequence_of_target = [int(number) for number in input().split()]
command = input().split(" ")

while command[0] != "End":

    action, index, value = command[0], int(command[1]), int(command[2])

    if action == "Shoot":
        sequence_of_target = shoot(sequence_of_target, index, value)

    elif action == "Add":
        sequence_of_target = add(sequence_of_target, index, value)

    elif action == "Strike":
        sequence_of_target = strike(sequence_of_target, index, value)

    command = input().split()


print(*sequence_of_target, sep= "|")


