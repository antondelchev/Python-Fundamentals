def loading_bar(num):
    loading = f"{num}% ["
    bars = num // 10
    for i in range(1, bars + 1):
        loading += "%"
        print(end="")
    loading += "." * (10 - bars)
    print(end="")
    loading += "]"

    if not num == 100:
        print(loading)
        return "Still loading..."
    elif num == 100:
        print("100% Complete!")
        return "[%%%%%%%%%%]"


number = int(input())
print(loading_bar(number))
