def factorial(a:int) ->int:

    for i in range(1, a):
        a *= i
    return a

number = int(input())
number_two = int(input())
result = factorial(number) // factorial(number_two)
print(f"{result:.2f}")