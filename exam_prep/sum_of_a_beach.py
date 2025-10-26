initial_string = input()

initial_string_lower_case = initial_string.lower()

partition_count = 0

if "sand" in initial_string_lower_case:
    partition_count += initial_string_lower_case.count("sand")

if "water" in initial_string_lower_case:
    partition_count += initial_string_lower_case.count("water")

if "fish" in initial_string_lower_case:
    partition_count += initial_string_lower_case.count("fish")

if "sun" in initial_string_lower_case:
    partition_count += initial_string_lower_case.count("sun")

print(partition_count)
