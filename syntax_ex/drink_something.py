ages = int(input())
drink = "drink "

if ages < 15:
    drink += "toddy"

elif ages < 19:
    drink += "coke"

elif ages < 22:
    drink += "beer"

else:
    drink += "whisky"

print(drink)