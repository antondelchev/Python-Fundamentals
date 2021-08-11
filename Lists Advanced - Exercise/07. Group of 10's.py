nums = [int(el) for el in input().split(", ")]

max_num = max(nums)
number_of_groups = max_num // 10

front = 0
back = 10

if max_num > number_of_groups * 10:
    number_of_groups += 1

for _ in range(1, number_of_groups + 1):
    group = []
    print(f"Group of {back}'s: [", end="")

    for el in nums:
        if front < el <= back or el == 0:
            group.append(el)

    print(*group, sep=", ", end="")
    print("]")

    front += 10
    back += 10
