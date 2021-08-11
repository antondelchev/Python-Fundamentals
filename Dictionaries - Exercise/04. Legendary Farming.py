inventory = {"fragments": 0, "shards": 0, "motes": 0}

shadowmourne = 0
valanyr = 0
dragonwrath = 0
crafted = False

loot = input().split()

while shadowmourne < 250 or valanyr < 250 or dragonwrath < 250:
    quantity = 0
    item = ""

    for el in range(0, len(loot), 2):
        quantity = int(loot[el])
        item = str(loot[el + 1]).lower()
        if item not in inventory:
            inventory[item] = quantity
        else:
            inventory[item] += quantity

        if item == "shards":
            shadowmourne += quantity
        elif item == "fragments":
            valanyr += quantity
        elif item == "motes":
            dragonwrath += quantity

        if dragonwrath >= 250 or valanyr >= 250 or shadowmourne >= 250:
            crafted = True
            break
    if crafted:
        break

    loot = input().split()

if dragonwrath >= 250:
    for el in inventory:
        if el == "motes":
            inventory[el] -= 250
    print("Dragonwrath obtained!")
elif valanyr >= 250:
    for el in inventory:
        if el == "fragments":
            inventory[el] -= 250
    print("Valanyr obtained!")
elif shadowmourne >= 250:
    for el in inventory:
        if el == "shards":
            inventory[el] -= 250
    print("Shadowmourne obtained!")

key_mats = {}
other_mats = {}

for key in inventory:
    if key == "motes" or key == "shards" or key == "fragments":
        key_mats[key] = inventory.get(key)
    else:
        other_mats[key] = inventory.get(key)

sorted_main_mats = sorted(key_mats.items(), key=lambda x: (-x[1], x[0]))
sorted_other_mats = sorted(other_mats.items(), key=lambda x: x[0])

[print(f"{el[0]}: {el[1]}") for el in sorted_main_mats]
[print(f"{el[0]}: {el[1]}") for el in sorted_other_mats]
