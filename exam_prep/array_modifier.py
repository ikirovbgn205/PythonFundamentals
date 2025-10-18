def swap(some_list:list, first_i:int, second_i:int)-> list:
    some_list[first_i], some_list[second_i] = some_list[second_i], some_list[first_i]
    return some_list

def multiply(some_list:list, first_i:int, second_i:int)-> list:
    result = some_list[first_i] * some_list[second_i]
    some_list[first_i] = result
    return some_list

def decrease(some_list:list)->list:
    for index in range(len(some_list)):
        some_list[index] -= 1
    return some_list

array_of_integers = list(map(int, input().split()))

command = input().split()

while command[0] != "end":


    if command[0] == "swap":
        index_one, index_two = int(command[1]), int(command[2])
        array_of_integers = swap(array_of_integers, index_one, index_two)

    elif command[0] == "multiply":
        index_one, index_two = int(command[1]), int(command[2])
        array_of_integers = multiply(array_of_integers, index_one, index_two)

    elif command[0] == "decrease":
        array_of_integers = decrease(array_of_integers)

    command = input().split()

print(*array_of_integers, sep=", ")