word = list(input())
ex = "aouei"

no_vow = [letter for letter in word if letter not in ex]
print("".join(no_vow))
