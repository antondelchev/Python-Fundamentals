import re

sentence = input()
word = input()

pattern = rf"\b{word}\b"

matched = re.findall(pattern, sentence, re.IGNORECASE)

print(len(matched))
