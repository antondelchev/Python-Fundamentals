num = float(input())

if num == 0:
    print("zero")
elif num > 0:
    if num < 1:
        print("small ", end="")
    elif num > 1000000:
        print("large ", end="")
    print("positive")
elif num < 0:
    if num > -1:
        print("small ", end="")
    elif num < -1000000:
        print("large ", end="")
    print("negative")
