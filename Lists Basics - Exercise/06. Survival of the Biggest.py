import sys

nums = input()
n = int(input())

nums_as_list = nums.split()

min_num = sys.maxsize
position = 0

for i in range(1, n + 1):
    for j in range(1, len(nums_as_list) + 1):
        if int(nums_as_list[j - 1]) < min_num:
            min_num = int(nums_as_list[j - 1])
            position = j - 1

    nums_as_list.pop(position)

    min_num = sys.maxsize
    position = 0

print(", ".join(nums_as_list))
