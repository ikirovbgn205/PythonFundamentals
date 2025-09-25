number_of_lines = int(input())
numbers = []
filtered_numbers = []

for _ in range(number_of_lines):
    num = int(input())
    numbers.append(num)

command = input()
if command == "even":
    for number in numbers:
        if number % 2 == 0:
            filtered_numbers.append(number)
if command == "odd":
    for number in numbers:
        if number % 2 != 0:
            filtered_numbers.append(number)
if command == "negative":
    for number in numbers:
        if number < 0:
            filtered_numbers.append(number)
if command == "positive":
    for number in numbers:
        if number >= 0:
            filtered_numbers.append(number)

print(filtered_numbers)
