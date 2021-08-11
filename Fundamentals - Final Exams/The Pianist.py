num_of_pieces = int(input())
pieces_collection = {}

for _ in range(1, num_of_pieces + 1):
    name, composer, key = input().split("|")
    pieces_collection[name] = {'composer': composer, 'key': key}

data = input()

while not data == "Stop":
    data = data.split("|")
    command = data[0]
    piece_name = data[1]

    if command == "Add":
        current_composer = data[2]
        current_key = data[3]
        if piece_name in pieces_collection:
            print(f"{piece_name} is already in the collection!")
        else:
            pieces_collection[piece_name] = {'composer': current_composer, 'key': current_key}
            print(f"{piece_name} by {current_composer} in {current_key} added to the collection!")
    elif command == "Remove":
        if piece_name in pieces_collection:
            pieces_collection.pop(piece_name)
            print(f"Successfully removed {piece_name}!")
        else:
            print(f"Invalid operation! {piece_name} does not exist in the collection.")
    elif command == "ChangeKey":
        new_key = data[2]
        if piece_name in pieces_collection:
            pieces_collection[piece_name]['key'] = new_key
            print(f"Changed the key of {piece_name} to {new_key}!")
        else:
            print(f"Invalid operation! {piece_name} does not exist in the collection.")

    data = input()

sorted_pieces = sorted(pieces_collection.items(), key=lambda x: (x[0], x[1]['composer']))

for composer_name, piece_info in sorted_pieces:
    print(f"{composer_name} -> Composer: {piece_info['composer']}, Key: {piece_info['key']}")
