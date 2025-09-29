numbers = input().split(" ")
count_numbers = int(input())
lst_of_integers = []


for number in numbers:
    lst_of_integers.append(int(number))

for _ in range(count_numbers):
    lst_of_integers.remove(min(lst_of_integers))

new_lst_of_str = []

for number in lst_of_integers:
    new_lst_of_str.append(str(number))

print(', '.join(new_lst_of_str))



