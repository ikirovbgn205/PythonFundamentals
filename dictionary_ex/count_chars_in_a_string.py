word = input()

chars = [char for char in word]

chars_counter = {}

exclusive_char = ' '

for char in chars:
    if char == exclusive_char:
        continue
    if char not in chars_counter.keys():
        chars_counter[char] = 1
    else:
        chars_counter[char] += 1

for key, value in chars_counter.items():
    print(f"{key} -> {value}")