def check_for_palindrome_num(list_of_nums):
    nums_list = str(list_of_nums).split(", ")
    for i in range(len(nums_list)):
        if i < len(nums_list) - 1:
            if nums_list[i] == nums_list[i][::-1]:
                print("True")
            else:
                print("False")
        elif i == len(nums_list) - 1:
            if nums_list[i] == nums_list[i][::-1]:
                return "True"
            else:
                return "False"


list_of_numbers = input()
print(check_for_palindrome_num(list_of_numbers))
