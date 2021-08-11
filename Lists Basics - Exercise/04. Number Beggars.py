nums = input()
beggars = int(input())

num_list = nums.split(", ")
collected_nums = []

for i in range(1, len(num_list) + 1):
    collected_current = 0

    if len(collected_nums) == beggars:
        break

    for j in range(i, len(num_list) + 1, beggars):
        collected_current += int(num_list[j - 1])

    collected_nums.append(collected_current)

if beggars > len(num_list):
    diff = beggars - len(num_list)
    for i in range(1, diff + 1):
        collected_nums.append(0)

print(collected_nums)
