string_values = input().split()

integer_values = []

for i in range(len(string_values)):
    integer_values.append(float(string_values[i]))

absolute_values = []

for index in range(len(integer_values)):
    absolute_values.append(abs(integer_values[index]))

print(absolute_values)
