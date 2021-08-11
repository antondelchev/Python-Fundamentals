text = input().split()
str_only = "".join(text)
text_dict = {}

for el in str_only:
    if el not in text_dict:
        text_dict[el] = 1
    else:
        text_dict[el] += 1

for key in text_dict:
    print(f"{key} -> {text_dict[key]}")
