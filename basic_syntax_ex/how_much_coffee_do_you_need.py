number_of_coffees = 0

while True:

    command = input()

    if command == 'END':
        print(number_of_coffees)
        break

    if command == 'dog' or command == 'cat' or command == 'coding' or command == 'movie':
        number_of_coffees += 1

    elif command == 'DOG' or command == 'CAT' or command == 'CODING' or command == 'MOVIE':
        number_of_coffees += 2

    if number_of_coffees > 5:
        print(f"You need extra sleep")
        break

