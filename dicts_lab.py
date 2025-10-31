elements = input().split()

shop = {}

for i in range(0, len(elements), 2):
    item = elements[i]
    qty = int(elements[i + 1])
    shop[item] = qty


print(shop)