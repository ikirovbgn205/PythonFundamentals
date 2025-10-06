def perfect_number(number: int) -> str:
    sum_of_divisors = 0
    for divisor in range(1, number):
        if number % divisor == 0:
            sum_of_divisors += divisor

    if number == sum_of_divisors:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


number_for_checking = int(input())
result = perfect_number(number_for_checking)
print(result)