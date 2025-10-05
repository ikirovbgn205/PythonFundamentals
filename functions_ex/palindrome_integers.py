def is_palindrome(number_one: str)-> str :

    if number_one == number_one[::-1]:
        result = "True"
        return result
    else:
        result = "False"
        return result


list_of_numbers = input().split(", ")
list_of_answers = []
for number in list_of_numbers:
    check = is_palindrome(number)
    list_of_answers.append(check)

print('\n'.join(list_of_answers))









