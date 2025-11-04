materials = {"shards" : 0, "fragments": 0, "motes": 0}

legendary_item = ""

won_a_legendary_item = False

while not won_a_legendary_item:

    material = input().split()

    for index in range(0, len(material), 2):
        item = material[index + 1].lower()
        qty = material[index]
        if item not in materials:
            materials[item] = int(qty)
        else:
            materials[item] += int(qty)
        if materials["shards"] >= 250:
            won_a_legendary_item = True
            materials["shards"] -= 250
            legendary_item = "Shadowmourne"
        elif materials["fragments"] >= 250:
            won_a_legendary_item = True
            materials["fragments"] -= 250
            legendary_item = "Valanyr"
        elif materials["motes"] >= 250:
            won_a_legendary_item = True
            materials["motes"] -= 250
            legendary_item = "Dragonwrath"
        if won_a_legendary_item:
            break

print(f"{legendary_item} obtained!")
for material, quantity in materials.items():
    print(f"{material}: {quantity}")


