initial_string = input().split()

total = 0

first_string = initial_string[0]
second_string = initial_string[1]


if len(first_string) > len(second_string):
    for index in range(len(second_string)):
        total += ord(first_string[index]) * ord(second_string[index])
    for index in range(len(second_string), len(first_string)):
        total += ord(first_string[index])

elif len(second_string) > len(first_string):
    for index in range(len(first_string)):
        total += ord(first_string[index]) * ord(second_string[index])
    for index in range(len(first_string), len(second_string)):
        total += ord(second_string[index])

else:
    for index in range(len(first_string)):
        total += ord(first_string[index])  * ord(second_string[index])


print(total)



