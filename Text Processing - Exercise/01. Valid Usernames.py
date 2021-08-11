usernames = input().split(", ")
valid_usernames = []

for name in usernames:
    counter = 0
    if 3 <= len(name) <= 16:
        counter += 1
    for el in name:
        if el.isdigit():
            pass
        elif el.isalpha():
            pass
        elif el == "-" or el == "_":
            pass
        else:
            counter -= 1

    if counter == 1:
        valid_usernames.append(name)

for names in valid_usernames:
    print(names)
