n = int(input())

pieces_info = {}

for _ in range(n):
    piece, artist, music_key = input().split("|")
    pieces_info[piece] = {"composer": artist, "piece_key": music_key}

command = input()

while not command == "Stop":
    info = command.split("|")
    piece = info[1]
    if info[0] == "Add":
        composer = info[2]
        key = info[3]
        if pieces_info.get(piece):
            print(f"{piece} is already in the collection!")
        else:
            pieces_info[piece] = {"composer": composer, "piece_key": key}
            print(f"{piece} by {composer} in {key} added to the collection!")
    elif info[0] == "Remove":
        if pieces_info.get(piece):
            pieces_info.pop(piece)
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif info[0] == "ChangeKey":
        new_key = info[2]
        if pieces_info.get(piece):
            pieces_info[piece]["piece_key"] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    command = input()

sorted_pieces = sorted(pieces_info.items(), key=lambda x: (x[0], x[1]["composer"]))

for name, info in sorted_pieces:
    print(f"{name} -> Composer: {info['composer']}, Key: {info['piece_key']}")
