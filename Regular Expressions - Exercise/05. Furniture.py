import re

info = input()

pattern = r">>(?P<name>[a-zA-Z]+)<<(?P<price>\d+(\.\d+)?)\!(?P<quantity>\d+)"
furniture = []
money_spent = 0

while not info == "Purchase":
    matched = re.match(pattern, info)
    if matched:
        furniture_item = matched.groupdict()
        furniture.append(furniture_item["name"])
        money_spent += float(furniture_item["price"]) * int(furniture_item["quantity"])

    info = input()

print("Bought furniture:")
if furniture:
    print("\n".join(furniture))
print(f"Total money spend: {money_spent:.2f}")
