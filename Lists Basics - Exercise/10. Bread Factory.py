events = input().split("|")
energy = 100
coins = 100
closed = False

for event in events:
    event_info = event.split("-")
    command = event_info[0]
    amount = int(event_info[1])
    if command == "rest":
        if energy + amount <= 100:
            energy += amount
            print(f"You gained {amount} energy.")
        elif energy + amount > 100:
            gained = 100 - energy
            energy += gained
            print(f"You gained {gained} energy.")
        elif energy == 100:
            print(f"You gained 0 energy.")
        print(f"Current energy: {energy}.")
    elif command == "order":
        if energy >= 30:
            coins += amount
            energy -= 30
            print(f"You earned {amount} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coins - amount > 0:
            coins -= amount
            print(f"You bought {command}.")
        elif coins - amount <= 0:
            print(f"Closed! Cannot afford {command}.")
            closed = True
            break

if not closed:
    print(f"Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
