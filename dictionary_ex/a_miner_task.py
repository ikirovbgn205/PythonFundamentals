loot = {}

delivery = input()

command_count = 0
last_key = ""

while delivery != "stop":

    if command_count % 2 == 0:
        last_key = delivery
        if delivery not in loot.keys():
            loot[delivery] = 0
    else:
        loot[last_key] += int(delivery)

    command_count += 1

    delivery = input()

for resource, qty in loot.items():
    print(f"{resource} -> {qty}")