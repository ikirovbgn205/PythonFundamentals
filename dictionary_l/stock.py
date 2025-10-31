items = input().split()

inventory = {}

for i in range(0, len(items), 2):
    stoke = items[i]
    quantity = int(items[i + 1])
    inventory[stoke] = quantity

checking = input().split()

for element in checking:
    if element in inventory:
        print(f"We have {inventory[element]} of {element} left")
    else:
        print(f"Sorry, we don't have {element}")