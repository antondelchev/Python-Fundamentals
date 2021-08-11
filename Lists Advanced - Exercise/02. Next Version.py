version = input().split(".")

whole_num = "".join(version)
result = str(int(whole_num) + 1)
res_list = []

for el in result:
    res_list.append(el)
add_length = 0
for index in range(1, len(res_list) + add_length):
    res_list.insert(index + add_length, ".")
    add_length += 1

print("".join(res_list))
