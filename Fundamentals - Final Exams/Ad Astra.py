import re

info = input()
pattern = r"(\||#)(?P<food>[a-zA-Z\s]+)\1(?P<date>\d{2}\/\d{2}\/\d{2})\1(?P<calories>[0-9]{1,4}|10000])\1"

total_calories = 0
valid_matches = [obj.groupdict() for obj in re.finditer(pattern, info)]

for el in valid_matches:
    total_calories += int(el["calories"])

total_days = total_calories // 2000
print(f"You have food to last you for: {total_days} days!")

if valid_matches:
    for item in valid_matches:
        print(f"Item: {item['food']}, Best before: {item['date']}, Nutrition: {item['calories']}")
