import re

text = input()

pattern = r"w{3}\.[a-zA-Z0-9-]+(\.[a-z]+)+"
websites = []

while text:
    valid_matches = [obj.group() for obj in re.finditer(pattern, text)]
    if valid_matches:
        websites.extend(valid_matches)
    text = input()

print("\n".join(websites))
