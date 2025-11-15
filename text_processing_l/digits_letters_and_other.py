initial_string = input()

chars = ""
digits = ""
symbols = ""

for char in initial_string:
    if char.isdigit():
        digits += char
    elif char.isalpha():
        chars += char
    else:
        symbols += char

print(digits)
print(chars)
print(symbols)
