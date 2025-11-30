initial_text = input().split(" | ")
words_dictionary = {}
handing_words = []

for sentence in initial_text:
    sentence = sentence.split(": ")
    word = sentence[0]
    definition = sentence[1]
    if word not in words_dictionary:
        words_dictionary[word] = []
    words_dictionary[word].append(definition)

words_for_test = input().split(" | ")
command = input()

while True:

    if command == "Test":
        for word in words_for_test:
            if word in words_dictionary.keys():
                print(f"{word}:")
                for definition in words_dictionary[word]:
                    print(f"-{definition}")
        break

    elif command == "Hand Over":
        for word in words_dictionary.keys():
            handing_words.append(word)
        print(" ".join(handing_words))
        break
