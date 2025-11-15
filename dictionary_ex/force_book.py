force_book = {}

command = input()

while command != "Lumpawaroo":

    if "|" in command:
        action = command.split(" | ")
        force_side, force_user = action[0], action[1]
        force_user_is_part_of_sides = False
        for list_with_users in force_book.values():
            if force_user in list_with_users:
                force_user_is_part_of_sides = True
                break
        if not force_user_is_part_of_sides:
            if force_side not in force_book.keys():
                force_book[force_side] = []
            force_book[force_side].append(force_user)

        if force_user in force_book.values():
            continue


    elif "->" in command:
        action = command.split(" -> ")
        force_user, force_side = action[0], action[1]

        for list_with_users in force_book.values():
            if force_user in list_with_users:
                list_with_users.remove(force_user)

        if force_side not in force_book.keys():
            force_book[force_side] = []
        force_book[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")


    command = input()

for side, users in force_book.items():
    if users:
        print(f'Side: {side}, Members: {len(users)}')
    for user in users:
        print(f'! {user}')
