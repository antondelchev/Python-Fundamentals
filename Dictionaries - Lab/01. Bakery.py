food_quantities = input().split(" ")
food_dict = {}

for el in range(0, len(food_quantities), 2):
    food = food_quantities[el]
    quantity = food_quantities[int(el) + 1]
    food_dict[food] = int(quantity)

print(food_dict)
