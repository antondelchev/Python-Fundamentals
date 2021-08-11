n = int(input())

for i in range(1, n + 1):
    sum_of_digits = 0
    num_as_str = str(i)
    p = len(num_as_str)

    for j in range(0, len(num_as_str)):
        current_digit = num_as_str[j]
        sum_of_digits += int(current_digit)

    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        print(f"{i} -> True")
    else:
        print(f"{i} -> False")
