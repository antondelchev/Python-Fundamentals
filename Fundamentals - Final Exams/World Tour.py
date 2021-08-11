trip_stops = input()
command = input()

while not command == "Travel":
    if "Add" in command or "Remove" in command:
        command = command.split(" ")
        order = command[0]
        info = str(command[1]).split(":")
        if order == "Add":
            index = int(info[1])
            destination = info[2]
            if 0 <= index < len(trip_stops):
                trip_stops = list(trip_stops)
                trip_stops.insert(index, destination)
                trip_stops = "".join(trip_stops)
        elif order == "Remove":
            start_index = int(info[1])
            end_index = int(info[2])
            if 0 <= start_index < len(trip_stops) and 0 <= end_index < len(trip_stops):
                trip_stops = list(trip_stops)
                del trip_stops[start_index: end_index + 1]
                trip_stops = "".join(trip_stops)
    elif "Switch" in command:
        command = command.split(":")
        old_stop = command[1]
        new_stop = command[2]
        if old_stop in trip_stops:
            trip_stops = trip_stops.replace(old_stop, new_stop)
    print(trip_stops)
    command = input()

print(f"Ready for world tour! Planned stops: {trip_stops}")
