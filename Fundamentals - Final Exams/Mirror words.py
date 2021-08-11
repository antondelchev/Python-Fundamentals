import re

text = input()

pattern = r"(#|@)(?P<wordone>[a-zA-Z]{3,})\1\1(?P<wordtwo>[a-zA-Z]{3,})\1"

valid_matches = [obj.groupdict() for obj in re.finditer(pattern, text)]
words = [list(valid_matches[el].values()) for el in range(len(valid_matches))]
mirror_words = [words[_] for _ in range(len(words)) if words[_][0] == words[_][1][::-1]]

if valid_matches:
    print(f"{len(valid_matches)} word pairs found!")
else:
    print("No word pairs found!")

if mirror_words:
    print("The mirror words are:")
    for element in range(len(mirror_words)):
        print(*mirror_words[element], sep=" <=> ", end="")
        if element < len(mirror_words) - 1:
            print(end=", ")
else:
    print("No mirror words!")
