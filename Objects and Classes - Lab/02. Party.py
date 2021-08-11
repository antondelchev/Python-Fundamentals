class Party:
    def __init__(self):
        self.people = []


party = Party()
command = input()
while not command == "End":
    party.people.append(command)
    command = input()

going = ", ".join(party.people)
print(f"Going: {going}")
print(f"Total: {len(party.people)}")
