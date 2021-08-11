import re

names = input()

match_pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
matches = re.findall(match_pattern, names)

print(" ".join(matches))
