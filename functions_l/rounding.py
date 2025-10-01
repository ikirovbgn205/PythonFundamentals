string = input().split()

numbers_list = []

for i in range(len(string)):
    numbers_list.append(float(string[i]))

rounded_numbers_list = []
for i in range(len(numbers_list)):
    rounded_numbers_list.append(round(numbers_list[i]))

print(rounded_numbers_list)