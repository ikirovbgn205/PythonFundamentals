strings = input().split()

final_string = ""

for string in strings:
    final_string += len(string) * string

print(final_string)