import math

party_size = int(input())
days = int(input())

total_coins = 0

for i in range(1, days + 1):
    if i % 10 == 0:
        party_size -= 2
    if i % 15 == 0:
        party_size += 5
    total_coins += 50
    total_coins -= party_size * 2
    if i % 3 == 0:
        total_coins -= party_size * 3
    if i % 5 == 0:
        total_coins += party_size * 20
        if i % 3 == 0:
            total_coins -= party_size * 2

coins_each = math.floor(total_coins / party_size)
print(f"{party_size} companions received {coins_each} coins each.")
