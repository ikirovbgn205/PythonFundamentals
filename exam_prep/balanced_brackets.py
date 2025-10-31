number_of_lines = int(input())

counter_of_opening_brackets = 0
counter_of_closing_brackets = 0

list_of_symbols = []

for _ in range(number_of_lines):
    symbol = input()
    list_of_symbols.append(symbol)

for i in range(len(list_of_symbols)):
    if list_of_symbols[i] == "(":
        counter_of_opening_brackets += 1
        next_symbol = i + 1
        if list_of_symbols[n] == "(":
            print("UNBALANCED")
    elif list_of_symbols[i] == ")":
        counter_of_closing_brackets += 1
        next_symbol = i + 1
        if list_of_symbols[next_symbol] == ")":
            print("UNBALANCED")

counters_sum = counter_of_closing_brackets + counter_of_opening_brackets
if counter_of_opening_brackets % 2 == 0 and counter_of_closing_brackets % 2 == 0:
    print("BALANCED")
elif counters_sum % 2 != 0:
    print("UNBALANCED")
else:
    print("UNBALANCED")

