def merge(some_list:list, command:list) -> list:
    start_index, end_index = int(command[1]), int(command[2])
    if start_index not in range(len(some_list)):
        start_index = 0
    if end_index not in range(len(some_list)):
        end_index = len(some_list) - 1
    some_list[start_index] = "".join(some_list[start_index: end_index + 1])
    some_list = some_list[:start_index + 1] + some_list[end_index + 1 :]
    return some_list

def divide(some_list:list, command:list) -> list:
    index, partition = int(command[1]), int(command[2])
    element = some_list[index]
    partition_size = len(element) // partition
    count_of_partitions = 0
    partitioned_list = []
    for current_index in range(0, len(element) ,partition_size):
        count_of_partitions += 1
        if count_of_partitions == partition:
            current_partition = element[current_index:]
            partitioned_list.append(current_partition)
            break
        else:
            current_partition = element[current_index:current_index + partition_size]
            partitioned_list.append(current_partition)
    some_list = some_list[:index] + partitioned_list + some_list[index + 1:]
    return some_list


original_list_of_strings = input().split()
command = input()

while command != '3:1':
    command = command.split()
    action = command[0]
    if action == 'merge':
        original_list_of_strings = merge(original_list_of_strings, command)
    elif action == 'divide':
        original_list_of_strings = divide(original_list_of_strings, command)

    command = input()

print(" ".join(original_list_of_strings))