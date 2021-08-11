activation_key_raw = input()
command = input()

while not command == "Generate":
    command = command.split(">>>")
    if command[0] == "Contains":
        if command[1] in activation_key_raw:
            print(f"{activation_key_raw} contains {command[1]}")
        else:
            print("Substring not found!")
    elif command[0] == "Flip":
        start_index = int(command[2])
        end_index = int(command[3])
        activation_key_raw = list(activation_key_raw)
        for index in range(start_index, end_index):
            if command[1] == "Upper":
                upper = activation_key_raw[index].upper()
                activation_key_raw[index] = upper
            elif command[1] == "Lower":
                activation_key_raw[index] = activation_key_raw[index].lower()
        activation_key_raw = "".join(activation_key_raw)
        print(activation_key_raw)
    elif command[0] == "Slice":
        activation_key_raw = list(activation_key_raw)
        start_index = int(command[1])
        end_index = int(command[2])
        del activation_key_raw[start_index: end_index]
        activation_key_raw = "".join(activation_key_raw)
        print(activation_key_raw)

    command = input()

print(f"Your activation key is: {activation_key_raw}")
