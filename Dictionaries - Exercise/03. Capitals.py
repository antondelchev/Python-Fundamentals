countries = input().split(", ")
capitals = input().split(", ")

result = dict(zip(countries, capitals))

for key in result:
    print(f"{key} -> {result[key]}")
