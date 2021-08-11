text = input().split()

out = [el for el in text if len(el) % 2 == 0]

for el in out:
    print(el)
