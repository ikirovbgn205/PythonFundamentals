def letters(some_username:str, some_move:str)-> str:
    if some_move == "Lower":
        some_username = some_username.lower()
    elif some_move == "Upper":
        some_username = some_username.upper()
    return some_username


def reverse(some_username:str, first_index:int, last_index:int)-> str:
    reversed_part = some_username[first_index:last_index + 1]
    return reversed_part[::-1]


def substrings(some_username:str, some_substring:str)-> str:
    if some_substring in some_username:
        item = ''
        replacement = some_username.replace(some_substring, item)
        return replacement
    else:
        return f"The username {some_username} doesn't contain {some_substring}."

def replace(some_username:str, replacement_char:str) -> str:
    item = "-"
    replacement = some_username.replace(replacement_char, item)
    return replacement

def validator(some_username:str, validation_char:str) -> str:
    if validation_char in some_username:
        return "Valid username."
    else:
        return f"{validation_char} must be contained in your username."

usernames = input()
command = input().split()

while True:

    action = command[0]

    if action == "Registration":
        break

    elif action == "Letters":
        move = command[1]
        usernames = letters(usernames, move)
        print(usernames)

    elif action == "Reverse":
        start_index = int(command[1])
        end_index = int(command[2])
        if 0 <= start_index < len(usernames) and 0 <= end_index < len(usernames):
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
        validation = command[1]
        result = validator(usernames, validation)
        print(result)

    command = input().split()
