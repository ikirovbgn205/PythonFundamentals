budget = int(input())

spend = 0

while True:
    command = input()

    if command == "End":
        print("You bought everything needed.")
        break

    elif int(command) + spend > budget:
        print(f"You went in overdraft!")
        break

    spend += int(command)