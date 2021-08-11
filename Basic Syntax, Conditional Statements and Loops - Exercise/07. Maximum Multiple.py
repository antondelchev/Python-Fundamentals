import sys

divisor = int(input())
bound = int(input())

max_num = -sys.maxsize

for i in range(1, bound + 1):
    if i % divisor == 0 and i > max_num:
        max_num = i

print(max_num)
