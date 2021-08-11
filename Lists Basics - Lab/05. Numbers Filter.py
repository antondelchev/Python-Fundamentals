n = int(input())

all_nums = []
needed = []

for i in range(1, n + 1):
    nums = int(input())
    all_nums.append(nums)

command = input()

for i in range(len(all_nums)):
    if command == "positive":
        if all_nums[i] >= 0:
            needed.append(all_nums[i])
    elif command == "negative":
        if all_nums[i] < 0:
            needed.append(all_nums[i])
    elif command == "even":
        if all_nums[i] % 2 == 0:
            needed.append(all_nums[i])
    elif command == "odd":
        if not all_nums[i] % 2 == 0:
            needed.append(all_nums[i])

print(needed)
