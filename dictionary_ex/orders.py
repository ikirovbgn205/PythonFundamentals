my_products = {}

total_prices = {}

while True :
    command = input().split()
    if command[0] == "buy":
        break

    product_name, product_price, product_qty = command[0], command[1], command[2]

    if product_name not in my_products:
        my_products[product_name] = int(product_qty)
    else:
        my_products[product_name] += int(product_qty)


    total_prices[product_name] = float(product_price) *  my_products[product_name]


for product, price in total_prices.items():
    print(f"{product} -> {price:.2f}")
