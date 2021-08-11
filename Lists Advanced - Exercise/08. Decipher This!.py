secret_message = input().split()
message = []

for el in secret_message:
    el = list(el)
    num = ""
    for i in range(len(el)):
        if el[0].isdigit():
            num += el[0]
            el.pop(0)
    el.insert(0, chr(int(num)))
    a, b = el[1], el[-1]
    el.pop(-1)
    el.append(a)
    el.pop(1)
    el.insert(1, b)
    message.append("".join(el))

for el in message:
    print(el, end=" ")
