def factorial(num1, num2):
    fact_1 = 1
    fact_2 = 1

    for i in range(1, num1 + 1):
        fact_1 *= i
    for j in range(1, num2 + 1):
        fact_2 *= j

    return f"{fact_1 / fact_2:.2f}"


number_one = int(input())
number_two = int(input())
print(factorial(number_one, number_two))
