def reduce_or_increase(some_targets_list:list, reductor:int)-> list:
    for i in range(len(some_targets_list)):
        if not some_targets_list[i] == -1 and some_targets_list[i] > reductor:
            some_targets_list[i] = some_targets_list[i] - reductor
        elif not some_targets_list[i] == -1 and some_targets_list[i] <= reductor:
            some_targets_list[i] = some_targets_list[i] + reductor
    return some_targets_list

sequence_of_targets = list(map(int, input().split()))
last_shot_target = 0
shots_count = 0
while True:
    command = input()

    if command == "End":
        print(f"Shot targets: {shots_count} -> {' '.join(map(str, sequence_of_targets))}")
        break

    index = int(command)

    if index in range(len(sequence_of_targets)) and sequence_of_targets[index] != -1:
        shots_count += 1
        last_shot_target = sequence_of_targets[index]
        sequence_of_targets[index] = -1
        sequence_of_targets = reduce_or_increase(sequence_of_targets, last_shot_target)
