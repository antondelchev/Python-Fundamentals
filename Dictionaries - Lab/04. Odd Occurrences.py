words = input().split()
lower_words = [i.lower() for i in words]
words_dict = {}

for el in lower_words:
    if el not in words_dict:
        words_dict[el] = 1
    else:
        words_dict[el] += 1

filtered = []
for element in words_dict:
    if not words_dict[element] % 2 == 0:
        filtered.append(element.lower())
printed = []
for i in filtered:
    if i not in printed:
        print(i, end=" ")
        printed.append(i)
