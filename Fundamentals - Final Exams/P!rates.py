data_first = input()

targeted_cities = {}

while not data_first == "Sail":
    name, population, gold = data_first.split("||")
    population = int(population)
    gold = int(gold)
    if name in targeted_cities:
        targeted_cities[name]['population'] += population
        targeted_cities[name]['gold'] += gold
    else:
        targeted_cities[name] = {'population': population, 'gold': gold}
    data_first = input()

data_second = input()

while not data_second == "End":
    data_second = data_second.split("=>")
    command = data_second[0]
    town = data_second[1]

    if command == "Plunder":
        people = int(data_second[2])
        gold = int(data_second[3])
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        if targeted_cities[town]['population'] - people <= 0 or targeted_cities[town]['gold'] - gold <= 0:
            targeted_cities.pop(town)
            print(f"{town} has been wiped off the map!")
        else:
            targeted_cities[town]['population'] -= people
            targeted_cities[town]['gold'] -= gold

    elif command == "Prosper":
        gold_value = int(data_second[2])

        if gold_value < 0:
            print("Gold added cannot be a negative number!")
        else:
            targeted_cities[town]['gold'] += gold_value
            total_gold = targeted_cities[town]['gold']
            print(f"{gold_value} gold added to the city treasury. {town} now has {total_gold} gold.")

    data_second = input()

if targeted_cities:
    sorted_cities = sorted(targeted_cities.items(), key=lambda x: (-x[1]['gold'], x[0]))

    print(f"Ahoy, Captain! There are {len(targeted_cities)} wealthy settlements to go to:")
    for el in sorted_cities:
        print(f"{el[0]} -> Population: {el[1]['population']} citizens, Gold: {el[1]['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
