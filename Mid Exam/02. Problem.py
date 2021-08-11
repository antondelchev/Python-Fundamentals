biscuits = [el.strip() for el in input().split(", ")]

command = input()
while not command == "No More Money":
    info = [el.strip() for el in command.split()]
    order = info[0].strip()
    type_of_biscuit = info[1].strip()

    if order == "OutOfStock":
        for index, item in enumerate(biscuits):
            if item == type_of_biscuit:
                biscuits[index] = "None"
    elif order == "Required":
        index = int(info[2])
        if 0 <= index < len(biscuits) and not biscuits[index] == "None":
            biscuits[index] = type_of_biscuit
    elif order == "Last":
        biscuits.append(type_of_biscuit)

    command = input()

[print(el, end=" ") for el in biscuits if not el == "None"]
