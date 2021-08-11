n = int(input())

current_num = n + 1
num_as_str = str(current_num)
found = False
counter = 0

while not found:
    counter = 0
    if len(num_as_str) == 4:
        if num_as_str[0] == num_as_str[1]:
            counter += 1
        elif num_as_str[0] == num_as_str[2]:
            counter += 1
        elif num_as_str[0] == num_as_str[3]:
            counter += 1
        elif num_as_str[1] == num_as_str[2]:
            counter += 1
        elif num_as_str[1] == num_as_str[3]:
            counter += 1
        elif num_as_str[2] == num_as_str[3]:
            counter += 1

    elif len(num_as_str) == 3:
        if num_as_str[0] == num_as_str[1]:
            counter += 1
        elif num_as_str[0] == num_as_str[2]:
            counter += 1
        elif num_as_str[1] == num_as_str[2]:
            counter += 1

    if counter == 0:
        print(num_as_str)
        found = True
        break
    else:
        current_num += 1
        num_as_str = str(current_num)
