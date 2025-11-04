name_and_number = input()

phonebook = {}


while True:

    if "-" not in name_and_number:
        break
    command = name_and_number.split("-")
    name = command[0]
    number = command[1]
    phonebook[name] = number
    name_and_number = input()


searches = int(name_and_number)

for _ in range(searches):
    name = input()
    if name  in phonebook.keys():
        number = phonebook[name]
        print(f"{name} -> {phonebook[name]}")
    else:
        print(f'Contact {name} does not exist.')