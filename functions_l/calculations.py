def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a // b

def calculator(operator, a, b):
    if operator == 'add':
        return add(a, b)

    if operator == 'subtract':
        return subtract(a, b)

    if operator == 'multiply':
        return multiply(a, b)

    if operator == 'divide':
        return divide(a, b)

operator_ = input()
number_one = int(input())
number_two = int(input())

result = calculator(operator_, number_one, number_two)
print(result)

