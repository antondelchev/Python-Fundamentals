import re

text = input()
pattern = r"(=|/)(?P<destination>[A-Z]{1}[a-zA-Z][a-zA-Z]+)\1"
points = 0

valid_matches = [obj.groupdict() for obj in re.finditer(pattern, text)]
destinations = []

for el in valid_matches:
    points += int(len(el['destination']))
    destinations.append(el['destination'])

print(f"Destinations: {', '.join(destinations)}")
print(f"Travel Points: {points}")
