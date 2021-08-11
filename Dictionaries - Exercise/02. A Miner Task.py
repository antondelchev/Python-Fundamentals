mineral = input()
results = {}

while not mineral == "stop":
    quantity = input()
    if mineral not in results:
        results[mineral] = int(quantity)
    else:
        results[mineral] += int(quantity)

    mineral = input()

for el in results:
    print(f"{el} -> {results[el]}")
