message = input()
command = input()

while not command == "Decode":
    command = command.split("|")
    if command[0] == "Move":
        num_of_letters = int(command[1])
        cut = ""
        if 0 < num_of_letters < len(message):
            cut = message[0:num_of_letters]
            message = list(message)
            del message[0: num_of_letters]
            message.append(cut)
            message = "".join(message)
    elif command[0] == "Insert":
        index = int(command[1])
        value = command[2]
        if 0 <= index <= len(message):
            message = list(message)
            message.insert(index, value)
            message = "".join(message)
    elif command[0] == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        if substring in message:
            message = message.replace(substring, replacement)
    command = input()

print(f"The decrypted message is: {message}")
