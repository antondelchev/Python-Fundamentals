location = input().split("\\")

for el in location:
    if "." in el:
        el = el.split(".")
        file = el[0]
        extension = el[1]

        print(f"File name: {file}")
        print(f"File extension: {extension}")
