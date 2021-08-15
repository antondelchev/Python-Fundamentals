message_capacity = int(input())
message_records = {}
command = input()

while not command == "Statistics":
    info = command.split("=")
    order = info[0]

    if order == "Add":
        username = info[1]
        sent = int(info[2])
        received = int(info[3])
        if not message_records.get(username):
            message_records[username] = {"sent": sent, "received": received, "total": 0}
            message_records[username]["total"] += sent + received
    elif order == "Message":
        sender = info[1]
        receiver = info[2]
        if message_records.get(sender) and message_records.get(receiver):
            if message_records[sender]["total"] + 1 >= message_capacity:
                print(f"{sender} reached the capacity!")
                message_records[receiver]["received"] += 1
                message_records[receiver]["total"] += 1
                message_records.pop(sender)
            elif message_records[receiver]["total"] + 1 >= message_capacity:
                message_records[sender]["sent"] += 1
                print(f"{receiver} reached the capacity!")
                message_records.pop(receiver)
            else:
                message_records[sender]["sent"] += 1
                message_records[sender]["total"] += 1
                message_records[receiver]["received"] += 1
                message_records[receiver]["total"] += 1
    elif order == "Empty":
        username = info[1]
        if username == "All":
            message_records.clear()
        elif message_records.get(username):
            message_records.pop(username)

    command = input()

print(f"Users count: {len(message_records)}")
sorted_message_records = sorted(message_records.items(), key=lambda x: (-x[1]["received"], x[0]))

for name, info in sorted_message_records:
    total = info["sent"] + info["received"]
    print(f"{name} - {total}")
