num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

if num_1 < num_3 and num_2 < num_3:
    print(num_3)
elif num_3 < num_1 and num_2 < num_1:
    print(num_1)
else:
    print(num_2)
