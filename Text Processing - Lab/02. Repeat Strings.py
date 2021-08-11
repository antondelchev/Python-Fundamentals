text = input().split()

print("".join(("".join(word * len(word))) for word in text))
