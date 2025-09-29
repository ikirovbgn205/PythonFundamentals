planned_gifts = input().split(" ")

while True:
    command = input()
    command_lst = command.split()
    action = command_lst[0]

    if command == "No Money":
        break

    elif action == "OutOfStock":
        gift_part = command_lst[1]
        for i in range(len(planned_gifts)):
            if planned_gifts[i] == gift_part:
                planned_gifts[i] = "None"

    elif action == "Required":
        gift_part = command_lst[1]
        index_part = int(command_lst[2])
        if 0 <= index_part < len(planned_gifts):
            planned_gifts[index_part] = gift_part


    elif action == "JustInCase":
        gift_part = command_lst[1]
        if planned_gifts:
            planned_gifts[-1] = gift_part

adjusted_gifts = []
for gift in planned_gifts:
    if gift != "None":
        adjusted_gifts.append(gift)

print(" ".join(adjusted_gifts))

