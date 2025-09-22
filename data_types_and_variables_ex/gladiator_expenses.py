lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

# Counting the costs
expenses = 0

# Checking what's broken
helmet_is_broken = False
sword_is_broken = False
shield_is_broken = 0

for game in range(1, lost_fights + 1):

    if game % 3 == 0:
        sword_is_broken = True
        expenses += sword_price # Sword is broken
        if game % 2 == 0:
            expenses += helmet_price
            shield_is_broken += 1 # Shield Breaks
            expenses += shield_price # At this point Sword and Helmet are broken in one fight

    elif game % 2 == 0:
        helmet_is_broken = True
        expenses += helmet_price # Helmet is broken


    if shield_is_broken == 2:
        expenses += armor_price # Armor breaks every second time shield breaks
        shield_is_broken = 0

print(f'Gladiator expenses: {expenses:.2f} aureus')
