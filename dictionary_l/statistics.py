inventory = {}
total_qty = 0

command = input().split(":")

while command[0] != "statistics":
    item = command[0]
    qty = int(command[1])
    if item not in inventory:
        inventory[item] = qty
        total_qty += qty
    elif item in inventory:
        inventory[item] += qty
        total_qty += qty

    command = input().split(":")

print("Products in stock:")
for item, qty in inventory.items():
    print(f"- {item}: {qty}")
print(f"Total Products: {len(inventory)}")
print(f"Total Quantity: {sum(inventory.values())}")
