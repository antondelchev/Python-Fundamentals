string_one = input()
string_two = input()

list_one = list(string_one)
previous_word = string_one

for i in range(0, len(string_one)):
    list_one[i] = string_two[i]
    new_word = "".join(list_one)
    if not new_word == previous_word:
        print(new_word)
        previous_word = new_word
