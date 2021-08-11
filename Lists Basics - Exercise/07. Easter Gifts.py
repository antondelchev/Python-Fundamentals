gift_names = input()

gift_names_list = gift_names.split()
command = input()

while command != "No Money":
    command_list = command.split()

    if command_list[0] == "JustInCase":
        gift_names_list[-1] = command_list[1]

    elif command_list[0] == "Required" and 0 <= int(command_list[2]) < len(gift_names_list):
        gift_names_list[int(command_list[2])] = command_list[1]

    elif command_list[0] == "OutOfStock":
        for i in range(len(gift_names_list)):
            if command_list[1] == gift_names_list[i]:
                gift_names_list[i] = "None"

    command = input()

removed = 0
for i in range(len(gift_names_list)):
    if gift_names_list[i - removed] == "None":
        gift_names_list.pop(i - removed)
        removed += 1

print(" ".join(gift_names_list))
