string = input().split(" ")
lst = []

for element in string:
    opposite_number = -int(element)
    lst.append(opposite_number)

print(lst)