import re

text = input()
word_pattern = r"(\*{2}|\:{2})(?P<word>[A-Z][a-z][a-z]+)\1"
whole_pattern = r"(?P<whole>(?P<separator>(\*{2}|\:{2}))[A-Z][a-z][a-z]+(?P=separator))"
threshold = 1

valid_matches_word = [obj_1.groupdict() for obj_1 in re.finditer(word_pattern, text)]
valid_matches_whole = [obj_2.groupdict() for obj_2 in re.finditer(whole_pattern, text)]

words_only = []
cool = []

emojis = []
cool_emojis = []

for el in valid_matches_word:
    words_only.append(el["word"])

for element in text:
    if element.isdigit():
        threshold *= int(element)

for word in words_only:
    current_coolness = 0
    for letter in word:
        current_coolness += int(ord(letter))
    if current_coolness > threshold:
        cool.append(word)

print(f"Cool threshold: {threshold}")
print(f"{len(words_only)} emojis found in the text. The cool ones are:")

for element_1 in valid_matches_whole:
    emojis.append(element_1["whole"])
for current_word in cool:
    for current_emoji in emojis:
        if current_word in current_emoji:
            cool_emojis.append(current_emoji)

print(*cool_emojis, sep="\n")
