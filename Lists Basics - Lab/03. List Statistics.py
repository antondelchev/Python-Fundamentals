n = int(input())

positives = []
negatives = []

for i in range(1, n + 1):
    nums = int(input())
    if nums >= 0:
        positives.append(nums)
    else:
        negatives.append(nums)

print(positives)
print(negatives)
print(f"Count of positives: {len(positives)}. Sum of negatives: {sum(negatives)}")
