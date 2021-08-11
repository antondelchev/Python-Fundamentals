words_part = input().split(", ")
words = input().split(", ")

inside = []

for index in range(len(words_part)):
    for next_index in range(len(words)):
        if words_part[index] in words[next_index]:
            inside.append(words_part[index])
            break

print(inside)
