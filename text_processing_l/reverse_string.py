command = input()

while True:

    if command == "end":
        break

    print(f"{command} = {command[::-1]}")

    command = input()