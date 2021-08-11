import re

num_of_barcodes = int(input())

pattern = r"(?<=^)(@{1}#+)[A-Z][a-zA-Z0-9]{4,}[A-Z](@{1}#+)(?=$)"

for _ in range(num_of_barcodes):
    barcode = input()
    match = [obj.group() for obj in re.finditer(pattern, barcode)]
    if match:
        number = ""
        counter = 0
        for el in match[0]:
            if el.isdigit():
                number += el
                counter += 1
        if counter > 0:
            print(f"Product group: {number}")
        else:
            print("Product group: 00")
    else:
        print("Invalid barcode")
