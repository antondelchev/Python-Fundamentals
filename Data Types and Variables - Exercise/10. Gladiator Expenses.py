lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

expenses_total = 0
shield_counter = 0

for i in range(1, lost_fights + 1):
    if i % 2 == 0:
        expenses_total += helmet_price
    if i % 3 == 0:
        expenses_total += sword_price
    if i % 2 == 0 and i % 3 == 0:
        expenses_total += shield_price
        shield_counter += 1
        if shield_counter % 2 == 0:
            expenses_total += armor_price

print(f"Gladiator expenses: {expenses_total:.2f} aureus")
