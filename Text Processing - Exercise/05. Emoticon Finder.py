text = input()
icons = []

for position, element in enumerate(text):
    if element == ":":
        full_icon = text[position] + text[position + 1]
        icons.append(full_icon)

for el in icons:
    print(el)
