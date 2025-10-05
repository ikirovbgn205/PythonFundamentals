list_of_numbers = input().split()
numbers_in_integer = []

for number in list_of_numbers:
    numbers_in_integer.append(int(number))

result = sorted(numbers_in_integer)
print(result)