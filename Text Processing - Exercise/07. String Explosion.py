text = list(input())

strength = 0
index_counter = 0

for i in range(len(text)):
    try:
        if text[index_counter] == ">" and text[index_counter + 1].isdigit():
            strength += int(text[index_counter + 1])
            text.pop(index_counter + 1)
            continue

        if strength > 0:
            strength -= 1
            if not text[index_counter].isdigit() and not text[index_counter] == ">":
                text.pop(index_counter)
                continue

        index_counter += 1

    except IndexError:
        pass

print("".join(text))
