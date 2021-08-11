n = int(input())
all_cars = {}

for _ in range(n):
    car, mileage, fuel = input().split("|")
    mileage = int(mileage)
    fuel = int(fuel)

    all_cars[car] = {'mileage': mileage, 'fuel': fuel}

data = input()

while not data == "Stop":
    data = data.split(" : ")
    command = data[0]
    chosen_car = data[1]
    if command == "Drive":
        distance = int(data[2])
        needed_fuel = int(data[3])
        if needed_fuel <= all_cars[chosen_car]['fuel']:
            all_cars[chosen_car]['fuel'] -= needed_fuel
            all_cars[chosen_car]['mileage'] += distance
            print(f"{chosen_car} driven for {distance} kilometers. {needed_fuel} liters of fuel consumed.")
        else:
            print(f"Not enough fuel to make that ride")

        if all_cars[chosen_car]['mileage'] >= 100000:
            print(f"Time to sell the {chosen_car}!")
            all_cars.pop(chosen_car)

    elif command == "Refuel":
        refill_with = int(data[2])
        if all_cars[chosen_car]['fuel'] + refill_with <= 75:
            all_cars[chosen_car]['fuel'] += refill_with
            print(f"{chosen_car} refueled with {refill_with} liters")
        elif all_cars[chosen_car]['fuel'] + refill_with > 75:
            print(f"{chosen_car} refueled with {75 - all_cars[chosen_car]['fuel']} liters")
            all_cars[chosen_car]['fuel'] = 75
    elif command == "Revert":
        revert_with = int(data[2])
        if all_cars[chosen_car]['mileage'] - revert_with >= 10000:
            print(f"{chosen_car} mileage decreased by {revert_with} kilometers")
            all_cars[chosen_car]['mileage'] -= revert_with
        else:
            all_cars[chosen_car]['mileage'] = 10000

    data = input()

sorted_cars = sorted(all_cars.items(), key=lambda x: (-x[1]['mileage'], x[0]))

for el in sorted_cars:
    print(f"{el[0]} -> Mileage: {el[1]['mileage']} kms, Fuel in the tank: {el[1]['fuel']} lt.")
