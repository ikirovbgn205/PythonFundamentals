def addition(number_one: int, number_two: int,)-> int:
    result = number_one + number_two
    return result

def subtract(number_one:int, number_two:int, number_three:int )-> int:
    result = addition(number_one, number_two)
    subtracted_result = result - number_three
    return subtracted_result

first_number = int(input())
second_number = int(input())
third_number = int(input())

add_and_subtract = subtract(first_number, second_number, third_number)
print(add_and_subtract)