num_entries = int(input())

all_students = {}

for entry in range(1, num_entries + 1):
    student = input()
    grade = float(input())

    if student not in all_students:
        all_students[student] = grade
    else:
        all_students[student] += grade
        all_students[student] = all_students[student] / 2

all_students = sorted(all_students.items(), key=lambda x: x[1], reverse=True)

[print(f"{name} -> {average_grade:.2f}") for name, average_grade in all_students if average_grade >= 4.5]
