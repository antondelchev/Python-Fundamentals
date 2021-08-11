budget = float(input())
flour_price_kg = float(input())

one_liter_milks = flour_price_kg + 0.25 * flour_price_kg
remaining = budget
cozonac_recipe = flour_price_kg + flour_price_kg * 0.75 + one_liter_milks / 4

cozonacs_done = 0
colored_eggs = 0

while 0 < remaining <= budget and cozonac_recipe <= remaining:
    remaining -= cozonac_recipe
    cozonacs_done += 1
    colored_eggs += 3
    if cozonacs_done % 3 == 0:
        colored_eggs -= cozonacs_done - 2

print(f"You made {cozonacs_done} cozonacs! Now you have {colored_eggs} eggs and {remaining:.2f}BGN left.")
