import re

text = input()
pattern = r"\d+"

matched_elements = []

while text:
    matches = re.findall(pattern, text)
    matched_elements.extend(matches)
    text = input()

print(*matched_elements)
