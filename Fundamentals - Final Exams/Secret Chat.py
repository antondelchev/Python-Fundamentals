message = input()
command = input()

while not command == "Reveal":
    command = command.split(":|:")
    if command[0] == "InsertSpace":
        index = int(command[1])
        message = list(message)
        message.insert(index, " ")
        message = "".join(message)
    elif command[0] == "Reverse":
        substring = command[1]
        reversed_string = substring[::-1]
        if substring in message:
            message = message.replace(substring, "", 1)
            message = list(message)
            message.append(reversed_string)
            message = "".join(message)
        else:
            print("error")
            command = input()
            continue
    elif command[0] == "ChangeAll":
        substring_two = command[1]
        replacement = command[2]
        if substring_two in message:
            message = message.replace(substring_two, replacement)

    print(message)
    command = input()

print(f"You have a new text message: {message}")
