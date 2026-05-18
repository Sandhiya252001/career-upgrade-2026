import math
A=int(input())
B=int(input())
angle=math.degrees(math.atan(A/B))
print(str(round(angle)) + "\u00b0")
