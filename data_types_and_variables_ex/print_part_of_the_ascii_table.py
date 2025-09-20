start_index = int(input())
last_index = int(input())

chars = ''

for number in range(start_index, last_index + 1):
    if number == last_index:
        print(chr(number))
    else:
        print(chr(number), end=' ')
