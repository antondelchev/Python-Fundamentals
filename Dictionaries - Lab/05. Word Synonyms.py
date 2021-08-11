num_of_entries = int(input())
synonyms_dict = {}

for i in range(1, num_of_entries + 1):
    word = input()
    synonym = input()

    if word not in synonyms_dict:
        synonyms_dict[word] = synonym
    else:
        synonyms_dict[word] += ", "
        synonyms_dict[word] += synonym

for el in synonyms_dict:
    print(f"{el} - {synonyms_dict[el]}")
