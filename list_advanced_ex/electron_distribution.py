number_of_electrons = int(input())

filled_shells_list = []
number_of_shell = 0

while number_of_electrons > 0:
    number_of_shell += 1
    max_number_of_electrons_in_current_shell = 2 * number_of_shell ** 2
    if number_of_electrons >= max_number_of_electrons_in_current_shell:
        filled_shells_list.append(max_number_of_electrons_in_current_shell)
    else:
        filled_shells_list.append(number_of_electrons)
    number_of_electrons -= max_number_of_electrons_in_current_shell

print(filled_shells_list)