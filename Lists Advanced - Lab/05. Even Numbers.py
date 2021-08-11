nums = input().split(", ")

int_nums = list(map(int, nums))
all_even = [index for index in range(len(int_nums)) if int_nums[index] % 2 == 0]

print(all_even)
