deck = input()
shuffles = int(input())

deck_list = deck.split()

half_one = []
half_two = []

shuffled = half_one
counter = 0

for i in range(0, int(len(deck_list) / 2)):
    half_one.append(deck_list[i])
for j in range(int(len(deck_list) / 2), len(deck_list)):
    half_two.append(deck_list[j])

for num_shuffle in range(1, shuffles + 1):
    for i in range(1, len(half_two) + 1):
        shuffled.insert(i + counter, half_two[i - 1])
        counter += 1
    # next halves
    half_one = []
    half_two = []
    for i in range(0, int(len(shuffled) / 2)):
        half_one.append(shuffled[i])
    for j in range(int(len(shuffled) / 2), len(shuffled)):
        half_two.append(shuffled[j])

    if num_shuffle < shuffles:
        shuffled = half_one
    counter = 0

print(shuffled)
