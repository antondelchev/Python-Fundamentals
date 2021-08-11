def orders(order, quantity):
    if order == "coffee":
        return 1.50 * quantity
    elif order == "coke":
        return 1.40 * quantity
    elif order == "water":
        return 1.00 * quantity
    elif order == "snacks":
        return 2.00 * quantity


order_item = input()
quantity_value = int(input())

print(f"{orders(order_item, quantity_value):.2f}")
