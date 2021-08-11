def chars_in_range(char1, char2):
    all_char = ""
    for i in range(ord(char1) + 1, ord(char2)):
        all_char += chr(i)
        all_char += " "
    return all_char


first_character = input()
second_character = input()

print(chars_in_range(first_character, second_character))
