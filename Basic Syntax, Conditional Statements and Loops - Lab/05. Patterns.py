n = int(input())

stars = n

for row in range(1, n + 1):
    for columns in range(1, row + 1):
        print("*", end="")
    print()
for row_under in range(1, n):
    for columns_under in range(1, stars):
        print("*", end="")
    stars -= 1
    print()
