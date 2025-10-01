#Recipe
#Eggs: 1 pack
#Flour: 1 kilo
#Milk: 0.250 ml.


budget = float(input())

flour_price_per_kilo = float(input())
eggs_price_per_pack = flour_price_per_kilo * 0.75
milk_price_per_liter = flour_price_per_kilo + (flour_price_per_kilo * 0.25)
price_milk_for_recipe = milk_price_per_liter / 4

price_for_loaf_bread = flour_price_per_kilo + eggs_price_per_pack + price_milk_for_recipe
bread = 0
eggs = 0

while budget >= price_for_loaf_bread:
    budget -= price_for_loaf_bread
    bread += 1
    eggs += 3

    if bread % 3 == 0:
        eggs -= bread - 2

else:
    print(f"You made {bread} loaves of Easter bread! Now you have {eggs} eggs and {budget:.2f}BGN left.")

