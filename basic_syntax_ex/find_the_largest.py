number = input()
digits = list(number)
result = ''

while digits:
    max_number = '0'
    for d in digits:
        if d > max_number:
            max_number = d
    result += max_number
    digits.remove(max_number)

print(result)
