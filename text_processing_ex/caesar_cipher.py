text = input()

crypted_text = ""

for char in text:
    position = ord(char) + 3
    crypted_text += chr(position)

print(crypted_text)
