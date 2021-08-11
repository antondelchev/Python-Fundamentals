import re

text = input()
pattern = r"(^_|(?<=\s_))[a-zA-Z0-9]+\b"

valid_matches = [match_obj.group() for match_obj in re.finditer(pattern, text)]

print(*valid_matches, sep=",")
