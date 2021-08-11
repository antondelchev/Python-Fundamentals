raw_password = input()
command = input()

while not command == "Done":
    command = command.split(" ")
    if command[0] == "TakeOdd":
        new_pass = []
        [new_pass.append(el) for index, el in enumerate(raw_password) if not index % 2 == 0]
        raw_password = "".join(new_pass)
        print(raw_password)
    elif command[0] == "Cut":
        start_index = int(command[1])
        end_index = start_index + int(command[2])
        raw_password = list(raw_password)
        del raw_password[start_index: end_index]
        raw_password = "".join(raw_password)
        print(raw_password)
    elif command[0] == "Substitute":
        substring = command[1]
        substitute = command[2]
        if substring in raw_password:
            raw_password = raw_password.replace(substring, substitute)
            print(raw_password)
        else:
            print("Nothing to replace!")
    command = input()

print(f"Your password is: {raw_password}")
