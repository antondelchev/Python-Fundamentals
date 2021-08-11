num_of_commands = int(input())
parking = {}

while not num_of_commands == 0:
    command = input().split()
    name = command[1]
    if "register" in command:
        plate = command[2]
        if name not in parking:
            parking[name] = plate
            print(f"{name} registered {plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {parking[name]}")
    elif "unregister" in command:
        if name not in parking:
            print(f"ERROR: user {name} not found")
        else:
            parking.pop(name)
            print(f"{name} unregistered successfully")
    num_of_commands -= 1

for users in parking:
    print(f"{users} => {parking[users]}")
