cards = input()

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

remove_dash = cards.split("-")
clean = "".join(remove_dash).split(" ")
removed_a = 0
removed_b = 0

list_as_dict = (dict.fromkeys(clean))
no_duplicates_list = list(list_as_dict)

stop = False

for i in range(len(no_duplicates_list)):
    if len(a) < 7 or len(b) < 7:
        stop = True
        break
    if no_duplicates_list[i][0] == "A":
        for position_a in range(1, 12):
            if len(no_duplicates_list[i]) == 2:
                if int(no_duplicates_list[i][1]) == int(position_a):
                    a.pop(position_a - 1 - removed_a)
                    removed_a += 1
                    break
            if len(no_duplicates_list[i]) == 3:
                if "1" in no_duplicates_list[i] and "0" in no_duplicates_list[i]:
                    a.pop(9 - removed_a)
                    removed_a += 1
                    break
                if "1" in no_duplicates_list[i] and "1" in no_duplicates_list[i]:
                    a.pop(10 - removed_a)
                    removed_a += 1
                    break
    if no_duplicates_list[i][0] == "B":
        for position_b in range(1, 12):
            if len(no_duplicates_list[i]) == 2:
                if int(no_duplicates_list[i][1]) == int(position_b):
                    b.pop(position_b - 1 - removed_b)
                    removed_b += 1
                    break
            if len(no_duplicates_list[i]) == 3:
                if "1" in no_duplicates_list[i] and "0" in no_duplicates_list[i]:
                    b.pop(9 - removed_b)
                    removed_b += 1
                    break
                if "1" in no_duplicates_list[i] and "1" in no_duplicates_list[i]:
                    b.pop(10 - removed_b)
                    removed_b += 1
                    break

print(f"Team A - {len(a)}; Team B - {len(b)}")
if stop:
    print("Game was terminated")
