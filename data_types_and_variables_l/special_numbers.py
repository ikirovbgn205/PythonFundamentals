# Read the number
number = int(input())

for num in range(1, number + 1): # Iterate from 1 to number
    sum_of_digits = 0
    digits = num
    while digits > 0: # Calculate the sum of digits
        sum_of_digits += digits % 10
        digits = int(digits) // 10
# Print the result
    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        print(f'{num} -> True')
    else:
        print(f'{num} -> False')