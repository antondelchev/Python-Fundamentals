import math
import sys

snowballs_total = int(input())

highest_value = -sys.maxsize
current_snow = 0
current_time = 0
current_quality = 0

while snowballs_total > 0:
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    snowball_value = math.pow(int(snowball_snow / snowball_time), snowball_quality)

    if snowball_value > highest_value:
        highest_value = snowball_value
        current_snow = snowball_snow
        current_time = snowball_time
        current_quality = snowball_quality

    snowballs_total -= 1

print(f"{current_snow} : {current_time} = {int(highest_value)} ({current_quality})")
