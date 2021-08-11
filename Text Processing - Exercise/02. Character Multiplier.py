text = input().split()
total_sum = 0

if len(text[0]) == len(text[1]):
    for position in range(len(text[0])):
        result = ord(text[0][position]) * ord(text[1][position])
        total_sum += result
elif len(text[0]) > len(text[1]):
    for position in range(len(text[1])):
        result = ord(text[0][position]) * ord(text[1][position])
        total_sum += result
    for position in range(len(text[1]), len(text[0])):
        total_sum += ord(text[0][position])
else:
    for position in range(len(text[0])):
        result = ord(text[1][position]) * ord(text[0][position])
        total_sum += result
    for position in range(len(text[0]), len(text[1])):
        total_sum += ord(text[1][position])

print(total_sum)
