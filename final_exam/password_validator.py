wanted_password = input()

command = input()

while command != "Complete":

    action = command.split()

    if action[0] == "Make":
        index = int(action[2])
        if action[1] == "Upper":
            before = wanted_password[:index]
            after = wanted_password[index+ 1:]
            wanted_password = before + wanted_password[index].upper() + after
            print(wanted_password)

        elif action[1] == "Lower":
            index = int(action[2])
            if action[1] == "Lower":
                before = wanted_password[:index]
                after = wanted_password[index + 1:]
                wanted_password = before + wanted_password[index].lower() + after
                print(wanted_password)


    elif action[0] == "Insert":
        index, character = int(action[1]), action[2]
        if 0 <= index < len(wanted_password):
            insertion_part_one = wanted_password[:index]
            insertion_part_two = wanted_password[index:]
            wanted_password = insertion_part_one + character + insertion_part_two
            print(wanted_password)

    elif action[0] == "Replace":
        char, value = action[1], action[2]
        if char in wanted_password:
            replacement_value = ord(char) + int(value)
            wanted_password = wanted_password.replace(char, chr(replacement_value))
            print(wanted_password)


    elif action[0] == "Validation":
        if len(wanted_password) < 8:
            print("Password must be at least 8 characters long!")
        if not all(ch.isalnum() or ch == "_" for ch in wanted_password):
            print("Password must consist only of letters, digits and _!")
        if not any(ch.isupper() for ch in wanted_password):
            print("Password must consist at least one uppercase letter!")
        if not any(ch.islower() for ch in wanted_password):
            print("Password must consist at least one lowercase letter!")
        if not any(ch.isdigit() for ch in wanted_password):
            print("Password must consist at least one digit!")

    command = input()