num = int(input())

num_as_str = str(num)
list_num = list(num_as_str)

print("".join(sorted(list_num, reverse=True)))
