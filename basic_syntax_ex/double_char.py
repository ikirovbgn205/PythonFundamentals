while True :

    command = input()

    if command == "End":
        break

    elif command == "SoftUni":
        continue

    word = ""

    for char in range(len(command)):
        word += command[char] * 2
    else:
        print(word)
