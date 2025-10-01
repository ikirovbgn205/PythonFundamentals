COFFEE = 1.50
WATER = 1.00
COKE = 1.40
SNACKS = 2.00

def vending_machine(product: str, qty: int):
    if product == 'coffee':
        return COFFEE * qty

    elif product == 'water':
        return WATER * qty

    elif product == 'coke':
        return COKE * qty

    elif product == 'snacks':
        return SNACKS * qty

product_ = input()
qty_products = int(input())
result = vending_machine(product_, qty_products)
total_price = result
print(f'{total_price:.2f}')