number_of_iterations = int(input())

sum_of_chars = 0

for _ in range(number_of_iterations):
    char = input()
    sum_of_chars += ord(char)

print(f'The sum equals: {sum_of_chars}')
