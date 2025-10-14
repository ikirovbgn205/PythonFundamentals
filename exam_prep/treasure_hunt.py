def loot(current_treasure_chest:list, current_items:list) -> list:
    for current_item in current_items:
        if current_item not in current_treasure_chest:
            current_treasure_chest.insert(0, current_item)
    return current_treasure_chest

def drop(current_treasure_chest:list, current_index: int) -> list:
    if index in range(len(current_treasure_chest)):
        current_treasure_chest.append(current_treasure_chest.pop(current_index))
    return current_treasure_chest

def steal(current_treasure_chest:list, current_count:int) -> list:
    if current_count >= len(current_treasure_chest):
        print(", ".join(current_treasure_chest))
        current_treasure_chest = []
    else:
        start_stealing = len(current_treasure_chest) - current_count
        after_stealing = current_treasure_chest[start_stealing:]
        current_treasure_chest = current_treasure_chest[:start_stealing]
        print(", ".join(after_stealing))
    return current_treasure_chest


treasure_chest = input().split("|")
command = input().split()

while command[0] != "Yohoho!":

    if command[0] == "Loot":
        item = command[1:]
        treasure_chest = loot(treasure_chest, item)

    elif command[0] == "Drop":
        index = int(command[1])
        treasure_chest = drop(treasure_chest, index)

    elif command[0] == "Steal":
        count = int(command[1])
        treasure_chest = steal(treasure_chest, count)
    command = input().split()


if not treasure_chest:
    print("Failed treasure hunt.")

else:
    average_gain = sum(len(item) for item in treasure_chest) / len(treasure_chest)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")