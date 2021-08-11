command = input()
courses = {}

while not command == "end":
    command = command.split(" : ")
    course_name = command[0]
    student = command[1]
    if course_name not in courses:
        courses[course_name] = [student]
    else:
        courses[course_name].append(student)

    command = input()

courses = sorted(courses.items(), key=lambda x: -len(x[1]))

for course_name, students in courses:
    print(f"{course_name}: {len(str(students).split(', '))}")
    for name in sorted(students):
        print(f"-- {name}")
