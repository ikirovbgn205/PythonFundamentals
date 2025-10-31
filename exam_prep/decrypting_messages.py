first_integer = int(input())
number_of_lines = int(input())

message = []

for _ in range(number_of_lines):
    symbol = input()
    final_integer = ord(symbol) + first_integer
    message.append(chr(final_integer))

print("".join(message))