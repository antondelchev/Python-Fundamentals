products_list = input().split("|")

command = input()

while not command == "Shop!":
    info = command.split("%")
    order = info[0]

    if order == "Important":
        product = info[1]
        found = False
        for index, item in enumerate(products_list):
            if item == product:
                hold = products_list.pop(index)
                products_list.insert(0, hold)
                found = True
        if not found:
            products_list.insert(0, product)
    elif order == "Add":
        product = info[1]
        if product not in products_list:
            products_list.append(product)
        else:
            print("The product is already in the list.")
    elif order == "Swap":
        product_one = info[1]
        product_two = info[2]

        if product_one in products_list and product_two in products_list:
            p_1_index = products_list.index(product_one)
            p_2_index = products_list.index(product_two)

            products_list[p_1_index], products_list[p_2_index] = products_list[p_2_index], products_list[p_1_index]
        else:
            missing = ""
            if product_one in products_list:
                missing = product_two
            else:
                missing = product_one
            print(f"Product {missing} missing!")
    elif order == "Remove":
        product = info[1]
        if product not in products_list:
            print(f"Product {product} isn't in the list.")
        else:
            products_list.remove(product)
    elif order == "Reverse":
        products_list = sorted(products_list, reverse=True)

    command = input()

num = 1
for el in products_list:
    print(f"{num}. {el}")
    num += 1
