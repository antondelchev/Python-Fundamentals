num_of_entries = int(input())

capacity = 255
filled = 0

while num_of_entries > 0:
    liters = int(input())
    predicted = filled + liters

    if predicted <= capacity:
        filled += liters
    else:
        print("Insufficient capacity!")

    num_of_entries -= 1

print(filled)
