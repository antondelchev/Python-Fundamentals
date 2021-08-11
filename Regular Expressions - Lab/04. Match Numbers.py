import re

numbers = input()

pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"
valid_numbers = [match_obj.group() for match_obj in re.finditer(pattern, numbers)]

print(" ".join(valid_numbers))
