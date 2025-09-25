number_of_lines = int(input())
magic_word = input()

strings = []

for _ in range(number_of_lines):
    string = input()
    strings.append(string)
print(strings)

for i in range(len(strings) -1, -1, -1):
    element = strings[i]
    if magic_word not in element:
        strings.remove(element)
print(strings)
