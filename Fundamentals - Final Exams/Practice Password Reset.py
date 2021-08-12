initial_pass = input()

command = input()

while not command == "Done":
    info = command.split()

    if info[0] == "TakeOdd":
        new_pass = "".join([el for index, el in enumerate(initial_pass) if not index % 2 == 0])
        initial_pass = new_pass
        print(initial_pass)
    elif info[0] == "Cut":
        index_start = int(info[1])
        end_index = int(info[2]) + index_start
        string_to_remove = initial_pass[index_start: end_index]
        initial_pass = initial_pass.replace(string_to_remove, "", 1)
        print(initial_pass)
    elif info[0] == "Substitute":
        substring = info[1]
        substitute = info[2]
        if substring in initial_pass:
            while substring in initial_pass:
                initial_pass = initial_pass.replace(substring, substitute)
                print(initial_pass)
        else:
            print("Nothing to replace!")
    command = input()

print(f"Your password is: {initial_pass}")
