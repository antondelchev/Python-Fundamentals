import re

text = input()

pattern = r"(?P<Day>\d{2})(?P<Separator>[\.\-\/])(?P<Month>[A-Z]{1}[a-z]{2})(?P=Separator)(?P<Year>\d{4})"

valid_dates = [obj.groupdict() for obj in re.finditer(pattern, text)]

print("\n".join([f"Day: {dates['Day']}, Month: {dates['Month']}, Year: {dates['Year']}" for dates in valid_dates]))
