text = input()

counter = 0
length = 0

for position in range(len(text)):
    if counter == length - 1:
        break
    if text[counter] == text[counter + 1]:
        text = text.replace(text[counter] + text[counter + 1], text[counter])
    else:
        counter += 1
    length = len(text)

print(text)
