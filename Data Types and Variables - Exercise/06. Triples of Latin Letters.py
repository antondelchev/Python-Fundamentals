n = int(input())

for one in range(97, 97 + n):
    for two in range(97, 97 + n):
        for three in range(97, 97 + n):
            print(f"{chr(one)}{chr(two)}{chr(three)}")
