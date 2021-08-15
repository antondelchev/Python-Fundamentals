import re

num_of_inputs = int(input())

pattern = r"(?<=^)(.*)>(?P<numbers>[0-9][0-9][0-9])\|(?P<letter1>[a-z]" \
          r"[a-z][a-z])\|(?P<letter2>[A-Z][A-Z][A-Z])\|(?P<symbol>[^<>][^<>][^<>])<\1(?=$)"

for _ in range(num_of_inputs):
    info = input()
    current = [match.groupdict() for match in re.finditer(pattern, info)]
    if current:
        password = current[0]["numbers"] + current[0]["letter1"] + current[0]["letter2"] + current[0]["symbol"]
        print(f"Password: {password}")
    else:
        print("Try another password!")
