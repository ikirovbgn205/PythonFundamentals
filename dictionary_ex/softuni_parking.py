number_of_operations = int(input())

parking_lot = {}

for _ in range(number_of_operations):
    command = input().split()

    if command[0] == "register":
        username = command[1]
        plate = command[2]
        if username not in parking_lot.keys():
            parking_lot[username] = plate
            print(f"{username} registered {plate} successfully")
        elif username in parking_lot.keys() :
            print(f"ERROR: already registered with plate number {parking_lot[username]}")

    elif command[0] == "unregister":
        username = command[1]
        if username not in parking_lot.keys():
            print(f"ERROR: user {username} not found")
        elif username in parking_lot.keys():
            parking_lot.pop(username)
            print(f"{username} unregistered successfully")

for username, plate in parking_lot.items():
    print(f"{username} => {plate}")

