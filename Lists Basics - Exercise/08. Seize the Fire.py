fire_cells = input()
water = int(input())

fire_put_out = 0
total_effort = 0

fc_as_list = fire_cells.split("#")
cells_out = []

for i in range(len(fc_as_list)):
    fire_current_cell = ""
    not_valid = False

    # fc_as_list[i][j] check and set fire lvl
    for j in range(len(fc_as_list[i])):
        if "High" or "Low" or "Medium" in fc_as_list[i]:
            if 48 <= ord(fc_as_list[i][j]) <= 57:
                fire_current_cell += fc_as_list[i][j]

    # finish
    if "High" in fc_as_list[i]:
        if 81 <= int(fire_current_cell) <= 125:
            pass
        else:
            not_valid = True
    elif "Medium" in fc_as_list[i]:
        if 51 <= int(fire_current_cell) <= 80:
            pass
        else:
            not_valid = True
    elif "Low" in fc_as_list[i]:
        if 1 <= int(fire_current_cell) <= 50:
            pass
        else:
            not_valid = True

    if not not_valid:
        if water >= int(fire_current_cell):
            water -= int(fire_current_cell)
            fire_put_out += int(fire_current_cell)
            cells_out.append(fire_current_cell)

print("Cells:")
for i in range(len(cells_out)):
    print(f" - {cells_out[i]}")
print(f"Effort: {0.25 * fire_put_out:.2f}")
print(f"Total Fire: {fire_put_out}")
