happiness = input().split()
improve = int(input())

happiness_as_int = list(map(int, happiness))

improved_happiness = [el * 3 for el in happiness_as_int]
average_happiness = sum(improved_happiness) / len(improved_happiness)
above_average = [el for el in improved_happiness if el >= average_happiness]

if len(above_average) >= len(happiness_as_int) / 2:
    print(f"Score: {len(above_average)}/{len(happiness_as_int)}. Employees are happy!")
else:
    print(f"Score: {len(above_average)}/{len(happiness_as_int)}. Employees are not happy!")
