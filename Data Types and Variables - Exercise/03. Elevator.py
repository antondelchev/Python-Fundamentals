num_persons = int(input())
capacity = int(input())

transported = 0
trips = 0

while transported < num_persons:
    transported += capacity
    trips += 1

print(trips)
