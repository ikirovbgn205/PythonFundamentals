numbers = list(map(int, input().split(", ")))

found_indices = [i for i in range(len(numbers)) if numbers[i] % 2 == 0]
print(found_indices)