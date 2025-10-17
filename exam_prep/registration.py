def letters(some_username:str, some_move:str):
    if some_move == "Lower":
        some_username = some_username.lower()
        return some_username
    elif some_move == "Upper":
        some_username = some_username.upper()
        return some_username
    return None


def reverse(some_username:str, first_index:int, last_index:int):
    if first_index in range(len(some_username)) and not first_index < 0 and \
            last_index in range(len(some_username)) and not last_index < 0:
        reversed_part = some_username[first_index:last_index + 1]
        return reversed_part[::-1]
    return None

def substrings(some_username:str, substring:str):
    if substring in some_username:
        sub = some_username.partition(substring)
        some_username = [word for word in sub if word not in substring ]
        return "".join(some_username)
    else:
        return f"The username {some_username} doesn't contain {substring}."

def replace(some_username:str, replacement_char:str):
    item = "-"
    list = [char for char in some_username]
    for i in range(len(list)):
        if list[i] == replacement_char:
            list[i] = item
    some_username = ''.join(list)
    return some_username

def validator(some_username:str, validation_char:str):
    if validation_char in some_username:
        return "Valid username."
    else:
        return f"{validation_char} must be contained in your username."

usernames = input()
command = input().split()

while command[0] != "Registration":

    action = command[0]

    if action == "Letters":
        move = command[1]
        usernames = letters(usernames, move)
        print(usernames)

    elif action == "Reverse":
        start_index = int(command[1])
        end_index = int(command[2])
        result = reverse(usernames, start_index, end_index)
        print(result)

    elif action == "Substring":
        substring = command[1]
        result = substrings(usernames, substring)
        print(result)

    elif action == "Replace":
        char = command[1]
        usernames = replace(usernames, char)
        print(usernames)

    elif action == "IsValid":
        validation= command[1]
        result = validator(usernames, validation)
        print(result)

    command = input().split()
