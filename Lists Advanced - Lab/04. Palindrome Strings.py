words = input().split()
pal_word = input()

pal_list = [el for el in words if el == el[::-1]]
found_word = [word for word in pal_list if word == pal_word]

counter = 0
for el in pal_list:
    if el == pal_word:
        counter += 1

print(pal_list)
print(f"Found palindrome {counter} times")
