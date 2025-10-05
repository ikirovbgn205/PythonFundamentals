def characters(first_char:str, secound_char:str,) -> list:
    char_book = []
    for char in range(ord(first_char) + 1, ord(secound_char)):
        char_book.append(chr(char))
    return char_book

first_symbol = input()
second_symbol = input()
result = characters(first_symbol, second_symbol)
print(" ".join(result))
