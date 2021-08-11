command = input()
items = {}

while not command == "statistics":
    key, value = command.split(": ")
    if key not in items:
        items[key] = int(value)
    else:
        items[key] += int(value)
    command = input()

print("Products in stock:")
total_quantity = 0
for el in items:
    print(f"- {el}: {items[el]}")
    total_quantity += int(items[el])
print(f"Total Products: {len(items)}")
print(f"Total Quantity: {total_quantity}")
