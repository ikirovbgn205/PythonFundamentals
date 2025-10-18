sequence_of_numbers = list(map(int, input().split()))

average_sum = sum(sequence_of_numbers) / len(sequence_of_numbers)
above_average = [num for num in sequence_of_numbers if num > average_sum]

if above_average:
    top_five = sorted(above_average, reverse=True)[:5]
    print(" ".join(map(str, top_five)))

else:
    print("No")