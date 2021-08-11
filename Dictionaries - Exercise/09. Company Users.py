book = {}

command = input()
while not command == "End":
    command = command.split(" -> ")
    name = command[0]
    employee_id = command[1]

    if name not in book:
        book[name] = employee_id
    else:
        if employee_id not in book[name]:
            book[name] += f", {employee_id}"

    command = input()

book = sorted(book.items(), key=lambda kvp: kvp[0])

for names, employee_ids in book:
    print(f"{names}")
    employee_ids = str(employee_ids).split(", ")
    for el in employee_ids:
        print(f"-- {el}")
