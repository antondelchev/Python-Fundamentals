nums_as_str = input()

nums_list = nums_as_str.split()
opposite_list = []

for i in range(len(nums_list)):
    opposite = int(nums_list[i]) * (-1)
    opposite_list.append(opposite)

print(opposite_list)
