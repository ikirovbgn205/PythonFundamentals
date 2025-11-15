usernames = input().split(", ")

for username in usernames:
    valid_username = True

    if not (3 <= len(username) <= 16):
        valid_username = False

    for symbol in username:
        if not (symbol.isalnum() or symbol == "-" or symbol == "_"):
            valid_username = False
            break

    if " " in username:
        valid_username = False

    if valid_username:
        print(username)



