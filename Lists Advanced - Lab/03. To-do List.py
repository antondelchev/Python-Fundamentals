command = input()
all_notes = ["0"] * 10

while not command == "End":
    note_and_index = command.split("-")
    index = int(note_and_index[0]) - 1
    note = note_and_index[1]
    all_notes.pop(index)
    all_notes.insert(index, note)
    command = input()

print([el for el in all_notes if not el == "0"])
