factor = int(input())
count = int(input())

num_list = []
element = 0

while count > 0:
    element += factor
    num_list.append(element)
    count -= 1

print(num_list)
