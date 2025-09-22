group_size = int(input())
days = int(input())

# Saving the coins
coins = 0

# Iterate days
for day in range(1,days + 1):

    if day % 10 == 0:
        group_size -= 2 # Every 10th day group size decrease by 2

    if day % 15 == 0:
        group_size += 5 # Every 15th day group size increase by 5

    if day % 3 == 0:
        coins -= 3 * group_size # For motivation Party

    if day % 5 == 0:
        coins += 20 * group_size # Slaying the monster
        if day % 3 == 0:
            coins -= 2 * group_size # Additional spend for motivation Party

    coins += 50 # Daily coins prize
    coins -= 2 * group_size # Daily spend for food


print(f'{group_size} companions received {coins // group_size} coins each.')