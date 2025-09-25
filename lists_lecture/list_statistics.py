number_of_lines = int(input())
positive =[]
negative = []

for _ in range(number_of_lines):
    number = int(input())
    if number < 0:
        negative.append(number)
    else:
        positive.append(number)

count_positive = len(positive)
sum_negative = sum(negative)

print(positive)
print(negative)
print(f'Count of positives: {count_positive}')
print(f'Sum of negatives: {sum_negative}')
