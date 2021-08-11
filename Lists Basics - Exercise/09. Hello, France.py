items_and_prices = input()
budget = float(input())

items_and_prices_list = items_and_prices.split("|")
spent = 0.0
new_prices = []

for i in range(len(items_and_prices_list)):
    current_item = ""
    current_item_price = ""
    not_enough_money = False
    # check and set price
    for j in range(len(items_and_prices_list[i])):
        if "Clothes" or "Shoes" or "Accessories" in items_and_prices_list[i]:
            if 48 <= ord(items_and_prices_list[i][j]) <= 57:
                current_item_price += items_and_prices_list[i][j]
            if ord(items_and_prices_list[i][j]) == 46:
                current_item_price += "."
    # finish
    if "Clothes" in items_and_prices_list[i]:
        if 0 < float(current_item_price) <= 50.00 and float(current_item_price) <= budget:
            budget -= float(current_item_price)
            spent += float(current_item_price)
        else:
            not_enough_money = True

    elif "Shoes" in items_and_prices_list[i]:
        if 0 < float(current_item_price) <= 35.00 and float(current_item_price) <= budget:
            budget -= float(current_item_price)
            spent += float(current_item_price)
        else:
            not_enough_money = True

    elif "Accessories" in items_and_prices_list[i]:
        if 0 < float(current_item_price) <= 20.50 and float(current_item_price) <= budget:
            budget -= float(current_item_price)
            spent += float(current_item_price)
        else:
            not_enough_money = True

    if not not_enough_money:
        price = float(current_item_price)
        price += 0.4 * float(current_item_price)
        new_prices.append(f"{price:.2f}")

total_income = 0.0
for i in range(len(new_prices)):
    total_income += float(new_prices[i])

profit = total_income - spent
for i in range(len(new_prices)):
    print(new_prices[i], end=" ")
print()
print(f"Profit: {profit:.2f}")

if budget + total_income >= 150:
    print("Hello, France!")
else:
    print("Time to go.")
