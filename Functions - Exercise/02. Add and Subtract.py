def sum_nums(num1, num2):
    return num1 + num2


def subtract(num1, num2, num3):
    result = sum_nums(num1, num2)
    return result - num3


def add_and_subtract(num1, num2, num3):
    return subtract(num1, num2, num3)


first_num = int(input())
second_num = int(input())
third_num = int(input())

print(add_and_subtract(first_num, second_num, third_num))
