number = input().split()
number_in_integers = []
for number in number:
    number_in_integers.append(int(number))

minimum_number = min(number_in_integers)
maximum_number = max(number_in_integers)
sum_of_numbers = sum(number_in_integers)

print(f'The minimum number is {minimum_number}')
print(f'The maximum number is {maximum_number}')
print(f'The sum number is: {sum_of_numbers}')