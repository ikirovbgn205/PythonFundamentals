first_sequence = input().split(", ")
second_sequence = input().split(", ")

words_with_first_word =[]

for first_word in first_sequence:
    for second_word in second_sequence:
        if first_word in second_word:
            words_with_first_word.append(first_word)
            break


print(words_with_first_word)