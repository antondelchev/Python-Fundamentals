num_of_electrons = int(input())

shells = []
position = 1

while not num_of_electrons == 0:
    if num_of_electrons >= 2 * position * position:
        shells.append(2 * position * position)
        num_of_electrons -= 2 * position * position
        position += 1
    else:
        shells.append(num_of_electrons)
        num_of_electrons -= num_of_electrons

print(shells)
