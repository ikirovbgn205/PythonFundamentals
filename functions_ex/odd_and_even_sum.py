def odd_and_even_sums(number: str) -> str:
    even_sum = 0
    odd_sum = 0
    for digit in number:
        if int(digit) % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)

    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"

number_for_checking = input()
result = odd_and_even_sums(number_for_checking)
print(result)