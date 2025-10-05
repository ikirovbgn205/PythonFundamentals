def even_numbers(numbers:list)->list:
    even_numbers_list = []
    for number in numbers:
        if int(number) % 2 == 0:
            even_numbers_list.append(int(number))

    return even_numbers_list

numbers_in_string = input().split()
result = even_numbers(numbers_in_string)
print(result)
