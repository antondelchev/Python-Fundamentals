biscuits_per_worker_per_day = int(input())
num_of_workers = int(input())
biscuits_monthly_competing_factory = int(input())

total_produced = 0

for day in range(1, 31):
    if day % 3 == 0:
        current_produced = num_of_workers * biscuits_per_worker_per_day * 0.75
    else:
        current_produced = num_of_workers * biscuits_per_worker_per_day
    total_produced += int(current_produced)

difference = abs(total_produced - biscuits_monthly_competing_factory)

print(f"You have produced {total_produced} biscuits for the past month.")
if total_produced > biscuits_monthly_competing_factory:
    print(f"You produce {difference / biscuits_monthly_competing_factory * 100:.2f} percent more biscuits.")
else:
    print(f"You produce {difference / biscuits_monthly_competing_factory * 100:.2f} percent less biscuits.")
