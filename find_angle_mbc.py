import math

AB = int(input())
BC = int(input())

angle = math.degrees(math.atan2(AB, BC))   # atan2 is safe and standard
print(f"{round(angle)}\N{DEGREE SIGN}")