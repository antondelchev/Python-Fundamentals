def perfect_num(num):
    whole_divisors = []
    sum_of_all_divisors = 0
    for i in range(1, num + 1):
        if num % i == 0 and not num == i:
            whole_divisors.append(i)

    for j in range(len(whole_divisors)):
        num_int = int(whole_divisors[j])
        sum_of_all_divisors += num_int

    if sum_of_all_divisors == num:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


number = int(input())
print(perfect_num(number))
