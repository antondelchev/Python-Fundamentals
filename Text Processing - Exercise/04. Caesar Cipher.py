message = input()
encrypted_message = ""

for el in message:
    encrypted_el = chr(ord(el) + 3)
    encrypted_message += encrypted_el

print(encrypted_message)
