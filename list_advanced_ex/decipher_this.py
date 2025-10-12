secret_message = input().split(" ")

message = []

for word in secret_message:
    digits = [symbol for symbol in word if symbol.isdigit()]
    new_word = [index for index in word if index not in digits]
    new_word[0], new_word[-1] = new_word[-1], new_word[0]
    number = "".join(digits)
    char = chr(int(number))
    new_word.insert(0, char)
    message.append("".join(new_word))

print(" ".join(message))

