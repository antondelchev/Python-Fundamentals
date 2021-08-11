num_wagons = int(input())

train = [0] * num_wagons
command = input()

while not command == "End":
    command_list = command.split()
    if command_list[0] == "add":
        train[-1] += int(command_list[1])
    elif command_list[0] == "insert":
        train[int(command_list[1])] += int(command_list[2])
    elif command_list[0] == "leave":
        train[int(command_list[1])] -= int(command_list[2])

    command = input()

print(train)
