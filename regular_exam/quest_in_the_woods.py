days_of_adventure = int(input())
number_of_people = int(input())
energy = float(input())
water_per_day_per_person = float(input())
food_per_day_per_person = float(input())

total_water_required = water_per_day_per_person * number_of_people * days_of_adventure
total_food_required = food_per_day_per_person * number_of_people * days_of_adventure

no_energy = False

for day in range(1, days_of_adventure + 1):
    lost_energy = float(input())
    energy -= lost_energy

    if energy <= 0:
        no_energy = True
        break

    if day % 3 == 0:
        energy += energy * 0.10
        total_food_required -= total_food_required / number_of_people

    if day % 2 == 0:
        energy += energy * 0.05
        total_water_required -= total_water_required * 0.30

if no_energy:
    print(f"You will run out of energy. You will be left with {total_food_required:.2f} food and {total_water_required:.2f} water.")
else:
    print(f"You are ready for the quest. You will be left with {energy:.2f} energy!")


