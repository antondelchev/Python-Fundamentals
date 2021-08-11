products_and_prices = {}
products_and_quantities = {}

orders = input().split()
while not orders[0] == "buy":
    name = orders[0]
    price = float(orders[1])
    quantity = int(orders[2])
    if name not in products_and_quantities:
        products_and_quantities[name] = quantity
    else:
        products_and_quantities[name] += quantity

    products_and_prices[name] = price

    orders = input().split()

for item in products_and_prices:
    print(f"{item} -> {products_and_prices[item] * products_and_quantities[item]:.2f}")
