words = input().split()
my_dictionary = {}

for word in words:
    lower_word = word.lower()
    if lower_word not in my_dictionary:
        my_dictionary[lower_word] = 0
    my_dictionary[lower_word] += 1

for key, value in my_dictionary.items():
    if value % 2 != 0:
        print(key, end=" ")