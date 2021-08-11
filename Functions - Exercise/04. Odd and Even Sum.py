def odd_even_sum(num1):
    num_list = list(str(num1))
    even_sum = 0
    odd_sum = 0
    for i in range(len(num_list)):
        if int(num_list[i]) % 2 == 0:
            even_sum += int(num_list[i])
        else:
            odd_sum += int(num_list[i])

    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


number = int(input())
print(odd_even_sum(number))
