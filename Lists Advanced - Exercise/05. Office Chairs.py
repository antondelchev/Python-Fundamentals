num_of_rooms = int(input())

messages = []
free_chairs = 0

for i in range(1, num_of_rooms + 1):
    chairs_and_visitors = input().split(" ")
    chairs = chairs_and_visitors[0]
    visitors = chairs_and_visitors[1]
    if len(chairs) < int(visitors):
        messages.append(f"{int(visitors) - len(chairs)} more chairs needed in room {i}")
    else:
        free_chairs += len(chairs) - int(visitors)

if not messages:
    print(f"Game On, {free_chairs} free chairs left")
else:
    for el in messages:
        print(el)
