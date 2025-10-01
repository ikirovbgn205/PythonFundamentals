quantity =int(input())
days = int(input())

ornament_set_price = 2
tree_skirt = 5
tree_garland = 3
tree_lights = 15

total_cost = 0
total_spirit = 0

for current_day in range(1, days + 1):
    if current_day % 11 == 0:
        quantity += 2
    if current_day % 2 == 0:
        total_cost += quantity * ornament_set_price
        total_spirit += 5
    if current_day % 3 == 0:
        total_cost += quantity * (tree_skirt + tree_garland)
        total_spirit += 13
    if current_day % 5 == 0:
        total_cost += quantity * tree_lights
        total_spirit += 17
        if current_day % 3 == 0:
            total_spirit += 30
    if current_day % 10 == 0:
        total_cost += tree_skirt + tree_garland + tree_lights
        total_spirit -= 20
if days % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")
