text = input()

digits = ""
letters = ""
symbols = ""

for el in text:
    if el.isdigit():
        digits += el
    elif el.isalpha():
        letters += el
    else:
        symbols += el

print(digits)
print(letters)
print(symbols)
