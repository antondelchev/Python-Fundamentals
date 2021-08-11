num_of_plants = int(input())
plants = {}

for _ in range(1, num_of_plants + 1):
    name, rarity = input().split("<->")
    rarity = int(rarity)
    plants[name] = {'rarity': rarity, 'rating': [], 'average_rating': 0.00}

data = input()

while not data == "Exhibition":
    data = data.split(": ")
    command = data[0]
    info = data[1].split(" - ")
    plant_name = info[0]

    if plant_name in plants:
        if command == "Rate":
            rating = float(info[1])
            plants[plant_name]['rating'].append(rating)
        elif command == "Update":
            new_rarity = int(info[1])
            plants[plant_name]['rarity'] = new_rarity
        elif command == "Reset":
            plants[plant_name]['rating'] = []

    else:
        print("error")

    data = input()

for el in plants:
    average_rating = 0.00
    if len(plants[el]['rating']) > 0:
        average_rating = sum(plants[el]['rating']) / len(plants[el]['rating'])

    plants[el]['average_rating'] = average_rating

sorted_plants = dict(sorted(plants.items(), key=lambda x: (-x[1]['rarity'], -x[1]['average_rating'])))

print("Plants for the exhibition:")
for item in sorted_plants:
    print(f"- {item}; Rarity: {sorted_plants[item]['rarity']}; Rating: {sorted_plants[item]['average_rating']:.2f}")
