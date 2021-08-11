word = input()

text_length = len(word)

for i in range(text_length, 0, - 1):
    print(word[i - 1], end="")
