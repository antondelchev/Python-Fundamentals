def calculate(num1, num2, action):
    if action == "multiply":
        return num1 * num2
    elif action == "divide":
        return num1 // num2
    elif action == "add":
        return num1 + num2
    elif action == "subtract":
        return num1 - num2


action_between_nums = input()
first_num = int(input())
second_num = int(input())

print(calculate(first_num, second_num, action_between_nums))
