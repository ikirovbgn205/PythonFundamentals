bomb = input()

final_string = ""
power = 0

for index in range(len(bomb)):

    if bomb[index] == ">":
        final_string += ">"
        power += int(bomb[index + 1])

    elif power > 0:
        power -= 1

    else:
        final_string += bomb[index]

print(final_string)
