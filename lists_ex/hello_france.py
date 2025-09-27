collection_of_items = input().split('|')
budget = float(input())
ticket_price = 150
selling_price_list = []
total_shopping_sum = 0
total_selling_sum = 0

for item in collection_of_items:
    item_values = item.split('->')
    current_item, current_price = item_values[0], float(item_values[1])

    if budget < current_price:
        continue

    if current_item == 'Clothes' and current_price <= 50:
        budget -= current_price
        total_shopping_sum += current_price
        selling_price = current_price + (current_price * 0.4)
        total_selling_sum += selling_price
        selling_price_list.append(f"{selling_price:.2f}")

    elif current_item == 'Shoes' and current_price <= 35:
        budget -= current_price
        total_shopping_sum += current_price
        selling_price = current_price + (current_price * 0.4)
        total_selling_sum += selling_price
        selling_price_list.append(f"{selling_price:.2f}")

    elif current_item == 'Accessories' and current_price <= 20.50:
        budget -= current_price
        total_shopping_sum += current_price
        selling_price = current_price + (current_price * 0.4)
        total_selling_sum += selling_price
        selling_price_list.append(f"{selling_price:.2f}")

print(" ".join(selling_price_list))
profit = total_selling_sum - total_shopping_sum
print(f'Profit: {profit:.2f}')
budget += total_selling_sum
if budget >= ticket_price:
    print('Hello, France!')
else:
    print("Not enough money.")

