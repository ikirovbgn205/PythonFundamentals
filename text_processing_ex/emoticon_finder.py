text = input()

emoticons = []

for index in range(len(text)):
    if text[index] == ":":
        emoticon = f"{text[index]}{text[index + 1]}"
        emoticons.append(emoticon)

for emoticon in emoticons:
    print(emoticon)

