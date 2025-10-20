route_to_titan = input().split("||")

available_fuel = int(input())
available_ammo = int(input())
current_command_index = 0

command = route_to_titan[current_command_index]

while True:

    current_command = command.split()
    current_command_index += 1

    if current_command[0] == "Titan":
        print("You have reached Titan, all passengers are safe.")
        break

    elif current_command[0] == "Travel":
        distance = int(current_command[1])
        if available_fuel >= distance:
            available_fuel -= distance
            print(f"The spaceship travelled {distance} light-years.")
        else:
            print("Mission failed.")
            break

    elif current_command[0] == "Enemy":
        enemy_armour = int(current_command[1])
        if available_ammo >= enemy_armour:
            available_ammo -= enemy_armour
            print(f"An enemy with {enemy_armour} armour is defeated.")
        elif available_ammo < enemy_armour:
            running_fuel = 2 * enemy_armour
            if available_fuel >= running_fuel:
                available_fuel -= running_fuel
                print(f'An enemy with {enemy_armour} armour is outmaneuvered.')
            else:
                print("Mission failed.")
                break

    elif current_command[0] == "Repair":
        loot = int(current_command[1])
        refuel = loot
        reload = 2 * loot
        available_fuel += refuel
        available_ammo += reload
        print(f"Ammunitions added: {reload}.")
        print(f"Fuel added: {refuel}.")

    command = route_to_titan[current_command_index]